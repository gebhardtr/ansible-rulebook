#  Copyright 2023 Red Hat, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import asyncio
import os
from unittest.mock import patch

import pytest
from freezegun import freeze_time

from ansible_rulebook.action.control import Control
from ansible_rulebook.action.metadata import Metadata
from ansible_rulebook.action.run_module import RunModule
from ansible_rulebook.conf import settings

DUMMY_UUID = "eb7de03f-6f8f-4943-b69e-3c90db346edf"
RULE_UUID = "abcdef3f-6f8f-4943-b69e-3c90db346edf"
RULE_SET_UUID = "00aabbcc-1111-2222-b69e-3c90db346edf"
RULE_RUN_AT = "2023-06-11T12:13:10Z"
ACTION_RUN_AT = "2023-06-11T12:13:14Z"
HERE = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(HERE, "../../playbooks/inventory.yml")


def _validate(queue, metadata, status, rc):
    while not queue.empty():
        event = queue.get_nowait()
        if event["type"] == "Action":
            action = event

    required_keys = {
        "action",
        "action_uuid",
        "activation_id",
        "activation_instance_id",
        "reason",
        "rule_run_at",
        "run_at",
        "rule",
        "ruleset",
        "rule_uuid",
        "ruleset_uuid",
        "status",
        "type",
        "matching_events",
        "job_id",
        "playbook_name",
        "rc",
    }
    assert action["action"] == "run_module"
    assert action["action_uuid"] == DUMMY_UUID
    assert action["activation_id"] == settings.identifier
    assert action["run_at"] == ACTION_RUN_AT
    assert action["rule_run_at"] == metadata.rule_run_at
    assert action["rule"] == metadata.rule
    assert action["ruleset"] == metadata.rule_set
    assert action["rule_uuid"] == metadata.rule_uuid
    assert action["ruleset_uuid"] == metadata.rule_set_uuid
    assert action["status"] == status
    assert action["rc"] == rc
    assert action["type"] == "Action"
    assert action["matching_events"] == {"m_0": {"a": 1}, "m_1": {"b": 2}}

    assert len(set(action.keys()).difference(required_keys)) == 0


@freeze_time("2023-06-11 12:13:14")
@pytest.mark.asyncio
async def test_run_module():
    queue = asyncio.Queue()
    metadata = Metadata(
        rule="r1",
        rule_set="rs1",
        rule_uuid=RULE_UUID,
        rule_set_uuid=RULE_SET_UUID,
        rule_run_at=RULE_RUN_AT,
    )
    control = Control(
        queue=queue,
        inventory=INVENTORY_FILE,
        hosts=["localhost"],
        variables={"events": {"m_0": {"a": 1}, "m_1": {"b": 2}}},
        project_data_file="",
    )
    action_args = {
        "module_args": {"name": "Fred Flintstone"},
        "name": "ansible.eda.upcase",
    }

    with patch("uuid.uuid4", return_value=DUMMY_UUID):
        await RunModule(metadata, control, **action_args)()

    _validate(queue, metadata, "successful", 0)
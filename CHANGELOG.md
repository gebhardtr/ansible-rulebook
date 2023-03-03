
# Changelog


##  [Unreleased]

### Added

- Scheduled workflow and split long-run tests 
- Ansible_eda top key in variables 
- Temporal use cases and handle async responses from Drools 
- Time constraints in rules schema 
- group_by_attributes
- Support multiple actions for a rule
- Support for search/match/regex 
- Support for graceful shutdown, timeout to allow actions to complete
- Removed the echo command in favor of debug with msg
- Support for null type in conditions
- Support Jinja2 substitution in rule names

### Fixed

- get_java_version, add compatibility with macs and tests for check_jvm
- selectattr operator with negation using greater/less than operators
- select operator and comparing ints and floats
- preserve native types when doing jinja substitution
- inventory argument to the CLI is optional

### Removed

- Redis and durability 
- envvar for rules_engine


## [0.10.1] - 2023-01-25

### Added

- Support for vars namespace
- Support for negation
- Support for Floats 
- Log format and set the log stream for debug/verbose 
- A builtin action : echo 
- Cmdline option --print_events 
- New action: run_job_template 
- Support for in and contains in condition 
- Add more info to --version flag
- Add EDA prefix to environment variables
- Enable drools for python 3.11
- Combine hosts when running a module
- Combine the same playbook on multiple hosts

### Fixed

- Schema validation for empty additionalProperties
- Drools dependency for python3.11
- Remove the temporary directory

### Changed

- Configure controller API access 
- Switch the default rules engine back to drools 
- Print help if run without arguments 

### Removed

- Removed durable rules
- Remove call_action
- Removes get_facts

## [0.9.4] - 2022-10-18

## [0.9.3] - 2022-10-18

### Changed

Update minimal python version 
Improves error messages for unhandled events

### Removed

- get_facts for now

## [0.9.2] - 2022-10-15

## [0.9.1] - 2022-10-15

### Added

- Job details for eda-server usage 
- add arg to install devel collection

### Fixed

- Duplicate para after merge
- Shutdown action and add test for it

### Changed

- Always log each retry
- Disable gather facts
- Don't use {{ }} in conditions

## [0.9.0] - 2022-10-12

### Added

- Adds support for non-async event plugins using put_nowait
- Support storing facts per host

### Fixed

### Changed

- Cmdline --rules to --rulebook
- Lookup directory to rulebooks in collections
- Rename assert_fact to set_fact

## [0.8.0] - 2022-10-11

### Added

- Support for any and all conditions
- Log every run_playbook or run_module retry

### Fixed

- Multiple operator expressions

### Changed

- Rename ansible-events to ansible-rulebook
- One shutdown event stops all rulesets
- Run each ruleset in a separate asyncio task

## [0.7.0] - 2022-09-14

### Added

- Quotes around is defined
- Worker mode
- Allow to rerun a playbook on failure

### Removed

- Plus syntax of is defined

### Fixed

- An error msg 

## [0.6.0] - 2022-08-24

### Added

- Support for executing ansible modules as part of action
- Support to post_event for Drools
- Support var_root in multi events
- Support for embedded spaces

### Fixed

- Sending ansible events as they are received
- Error handling for the websocket connection

### Changed

- Use a dictionary for var_root with the old key: new key

## [0.5.1] - 2022-08-10

### Added

- `durable-rules` adapter invoking a REST service
- Support events in print\_event

### Fixed

-  a bug in non string type in facts

### Removed

- event\_filters folder under ansible\_events

## [0.5.0] - 2022-07-28


### Added

- Or operator
- Fact namespace to variable lookup
- Add operator
- json\_mode option for run\_playbook action
- Coroutine based event sources

### Fixed

- Async sources of hosts and range2

### Changed

- Argument for post\_event to event

## [0.4.0] - 2022-06-23

### Added

- Websocket event log

### Changed

- Converts actions to async functions


## [0.3.0] - 2022-05-06

### Added

- Error message for missing rules
- Collection support
- Schema for the ruleset files


## [0.2.0] - 2022-05-02

### Added

- Support for multiple sources
- Back plan
- Variable substitution to list args
- Greater than operator to conditions
- Copy files and fixes post\_events
- Support for comparing events and facts
- Booleans to condition parser
- Lists\_to\_dicts
- Event\_filters

### Fixed

- Log scraper
- Multiple hosts tests

### Changed

- Rules to a optional argument

## [0.1.2] - 2022-03-16

### Fixed

- Flushes standard output

## [0.1.1] - 2022-03-16

### Added

- Project structure
- Initial version of rule engine
- Tests for multiple and statements
- Support for enabled flag on rules
- Event source filters
- Fact as synonym for event in conditions
- Fact assignment in conditions
- Dpath to value access
- Check for size of dictionaries due to durable rules limitation
- Support for multiple conditions
- Support for 'is defined'
- Docopt to test requirements
- Dpath to requirements
- Rule parsing test
- Asserting facts from ansible facts
- Assert\_facts option to run\_playbook
- Pass by value in substitute\_variables
- Support substituting variables in dictionaries
- Support for matching all to inventory
- Performance tests
- Variables and facts to actions
- Support for host-specific rulesets
- Example rules
- Cli
- Requirements

### Fixed

- Filters with no args
- Typing
- URL on pypi
- Types

### Changed

- Fact to event in conditions
- Glob to var\_root
- Host\_ruleset to ruleset in ActionContext
- Generate\_rulesets to generate\_host\_rulesets
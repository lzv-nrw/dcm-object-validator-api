# Changelog

## [4.1.0] - 2024-10-11

### Added

- added /validation-DELETE endpoint for abort mechanism

## [4.0.0] - 2024-09-05

### Changed

- **Breaking:** update SelfDescription for scalable orchestration (`127c52fd`)
- **Breaking:** rename JobToken field 'token' to 'value' (`01cd52d4`)

## [3.0.2] - 2024-07-19

### Fixed

- removed unused references to bagit-profile in `SelfDescription` (`63b7a933`)
- fixed bad description in `SelfDescription.configuration.settings...plugins` (`8faafa24`)

## [3.0.0] - 2024-07-17

### Changed

- **Breaking:** refactored /identify-GET response to common DCM-format (`82b0a483`)
- **Breaking:** removed requirement for `JobData.valid` (`918832bd`)

## [2.0.0] - 2024-04-25

### Changed
- **Breaking:** renamed schema `DateTime` to `ISODateTime` (reserved by swagger codegen) (`8f66bae6`)
- **Breaking:** termination callback now returns with full json of JobToken (`e9226b1f`)
- **Breaking:** changed requestBody format for validation request (`7f57b94b`, `5e042d07`)
- **Breaking:** renamed validation endpoints (`d5b9b3e5`)
- **Breaking:** improved Report schema, now supports custom job output data format and Reports of child processes (`f12f2b24`, `b991bd29`, `7c45bbb5`, `117dc696`)
- **Breaking:** migrated to OpenAPI-generator for SDK generation (`e86cf67c`)

## [1.0.0] - 2024-01-25

### Changed
- **Breaking:**: change name of parameter 'validation_token' to 'token' (`ba228498`)
- changed the list of required properties in schemata (`6aa3a9d2`)
- **Breaking:**: change requestBody-property names to camel case (`ecf22c80`)
- use lzv.nrw domain for example urls (`3a85ebe2`)

### Added
- added extra html response status codes (`6a7b45c9`)

## [0.3.0] - 2024-01-18

### Changed

- initial release of dcm-object-validator-api

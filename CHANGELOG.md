# Change Log
All notable changes to this project will be documented in this file.

## 1.0.0 - 2020-02-28
### Added

### Changed

### Removed


## 0.9.0 - 2019-04-16
### Added
- The jobs() methods have been updated to detect the version of the Jobs API and, when appropriate, use the Aloe
  definition of the Jobs API.
- Support was added for managing Actor aliases through the listAliases(), getAlias(), addAlias(), and deleteAlias()
  functions.

### Changed
- The JSON definitions of the API resources have been split into separate physical files to simplify management.
- Exception handling in the process_model was updated so that, in the case where an API response does not agree with the
  corresponding model spec, the library will now return a Python object instead of an exception.

### Removed
- No change.


## 0.8.0 - 2018-12-13
### Added
- Authentication methods (i.e., `clients_create`, `get_access_token`).
- Methods to interact with `files` endpoints.

### Changed
- Updated documentation layout.
- Updated testing framework.

### Removed
- No change.

## 0.7.3 - 2018-09-13
### Added
- No change.

### Changed
- Fixed issue where authentication does not honor AGAVE_CACHE_DIR (https://github.com/TACC/agavepy/issues/38)
- Fixed an issue where futures was missing from python2 requirements.

### Removed
- No change.


## 0.7.2 - 2018-07-03
### Added
- No change.

### Changed
- Fixed issue where importing the actors module failed due to missing cloudpickle dependency.

### Removed
- No change.


## 0.7.1 - 2018-07-01
### Added
- No change.

### Changed
- Fixed issue with clients.add where client was created but am Exception was raised trying to persist the client locally using shelve.

### Removed
- The legacy `save()` and `recover()` methods that leveraged the shelve package have been removed. This functionality has been replaced with the `Agave.restore()` and `Agave._write_client()` methods.


## 0.7.0 - 2018-03-08
### Added
- Added support for nonces including creating an Agave client using the `use_nonce=True` flag.
- Added support for managing an actor's state.
- Added support for managing an actor's permissions.

### Changed
- No change.

### Removed
- No change.


## 0.6.1 - 2017-11-6
### Added
- No change.

### Changed
- Fixed an issue in setup.py preventing pip install to work from within python 2.

### Removed
- No change.


## 0.6.0 - 2017-11-6
### Added
- Added support for Python 3.
- Added support for restoring an agavepy client from an Agave CLI cache file.

### Changed
- Fixed issue where associatedUuid was (erroneously) required for notifications.list().

### Removed
- No change.



## 0.5.0 - 2017-10-11
### Added
- Added support for job output utilities.
- Add support for creating agave clients within actors from JWT information.
- Add support for actor state updates.
- Add support for additional variables returned from the actors get_context() method.

### Changed
- No change.

### Removed
- No change.


## 0.4.0 - 2017-05-11
### Added
- Added support for streaming file uploads via the requests_toolbelt.

### Changed
- No change.

### Removed
- No change.


## 0.3.14 - 2016-10-13
### Added
- No change.

### Changed
- (#30) Fix bug in files.getHistory operation where systemId parameter was missing.

### Removed
- No change.


## 0.3.13 - 2016-09-20
### Added
- Added support for unprivileged metadata queries.

### Changed
- Improvements to test suite, including a Docker image for portability.

### Removed
- No change.


## 0.3.12 - 2016-08-29
### Added
- Added support for v2 of admin_password grant (role-based version).

### Changed
- Fixed issue with persisting existing clients to cache file.

### Removed
- No change.


## 0.3.11 - 2016-07-01
### Added
- Added support for enabling and disabling systems.

### Changed
- Fixed `path` parameter for files.manage operations.

### Removed
- No change.


## 0.3.10 - 2016-05-17
### Added
- Added support for http proxies.

### Changed
- No change.

### Removed
- No change.


## 0.3.9 - 2016-05-13
### Added
- Added support for token_callback on Agave object, to be called any time a token is refreshed.
- Added support for passing a headers object to any agavepy operation.
- Added support for search parameter to all get operations.
- Added support for passing a notifications to the files.importData operation.
- Added convenience method download_uri on the Agave client to download an agave URL or jobs output URL to an
absolute path on the local file system.

### Changed
- Fixed issues with permissions and roles definitions in swagger resources file.

### Removed
- No change.


## 0.3.8 - 2016-02-26
### Added
- Additional test coverage.

### Changed
- Fix geturl in case client is constructed with only an access token.
- Fixed status values in async module to align with Agave.
- Modified the test suite so that it can be run with different combinations of credentials.

### Removed
- No change.



## 0.3.7 - 2016-02-17
### Added
- Additional test coverage for files permissions.

### Changed
- Fixes to swagger definition impacting files permissions, postits, and profiles.
- Added limit and offset parameters to swagger definitions for endpoints returning collection listings.

### Removed
- No change.


## 0.3.6 - 2016-02-15
### Added
- No change

### Changed
- Fixed bug uploading binary files.

### Removed
- No change.


## 0.3.5 - 2016-02-09
### Added
- async.py, module with convenience class for handling.
- significant increase in tests.

### Changed
- Fixed issue where boolean parameters were being ignored.
- Fixed issues in the Notification model preventing basic use of that service.
- Fixed issues in the Profile model preventing basic use of that service.
- Fixed issues in the Metadata model preventing basic use of that service.
- Fixed issue with public/private parameter definition for systems.
- Fixed issue where error was returned if services (properly) returned an empty response.


### Removed
- No change.


## 0.3.4 - 2016-02-04
### Added
- No change

### Changed
- Fixed issue with token auto-refresh failing for tenants with v 1.9 of APIM.

### Removed
- No change.


## 0.3.3 - 2016-02-04
### Added
- Project CHANGELOG.md file.

### Changed
- Fixed issues publishing to PyPI, including URL and requirements.
- Fixed README to refer to github project home.

### Removed
- No change.

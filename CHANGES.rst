Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

v2.0.4.2
--------
2022-06-01: update to github actions checkout@v3 and setup-python@v3

v2.0.4.1
--------
2022-06-01: update github actions test matrix

v2.0.4
--------
2022-03-29: remedy mypy Untyped decorator makes function "cli_info" untyped

v2.0.3
--------
2022-03-25: fix github actions windows test

v2.0.1
--------
2021-11-22: Patch Release
    - fix tests

v2.0.0
--------
2021-11-22: Major Release
    - fix "setup.py test"
    - delete some (old) functions

v1.2.0
--------
2021-11-22: Minor Release
    - implement github actions
    - deduplicate code, added lib_detect_testenv as dependency
    - deleted functions which reside now in lib_detect_testenv

v1.1.8
--------
2020-10-09: service release
    - update travis build matrix for linux 3.9-dev
    - update travis build matrix (paths) for windows 3.9 / 3.10

v1.1.7
--------
2020-08-08: service release
    - fix documentation
    - fix travis
    - deprecate pycodestyle
    - implement flake8

v1.1.6
---------
2020-08-01: fix pypi deploy

v1.1.5
--------
2020-07-31: initial release

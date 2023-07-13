lib_programname
===============


Version v2.0.8 as of 2023-07-13 see `Changelog`_

|build_badge| |license| |jupyter| |pypi| |pypi-downloads| |black|

|codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/lib_programname/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/lib_programname/actions/workflows/python-package.yml


.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_programname/master?filepath=lib_programname.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-programname?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_programname

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_programname
   :target: https://codecov.io/gh/bitranox/lib_programname

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_programname?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_programname/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_programname?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_programname/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_programname?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_programname/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://snyk.io/test/github/bitranox/lib_programname/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_programname

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/lib-programname
   :target: https://pypi.org/project/lib-programname/
   :alt: PyPI - Downloads

This little Library returns the path of the executed Python Script.

Finding the name of the program from which a Python module is running can be trickier than it would seem at first, so lets make it damned easy.
This works under pycharm, pytest, pytest-docrunner, uwsgi, dreampie etc. correctly.

You might dive into Dough Hellmans `article <https://doughellmann.com/posts/determining-the-name-of-a-process-from-python/>`_
about that issue.

.. code-block::

    $> python -m pip install lib_programname
    $> python
    >>> import lib_programname
    >>> path_to_program = lib_programname.get_path_executed_script()    # type: pathlib.Path


This also works now if the script does not have any extension and if the scripts is symlinked.

In case the script is called via a symlink, the actual script location is returned, not the symlink !

.. code-block::

    $ # the test script
    $ cat test.py
    #!/usr/bin/env python3
    import lib_programname
    # this returns the fully resolved path to the launched python program
    path_to_program = lib_programname.get_path_executed_script()  # type: pathlib.Path
    print(path_to_program)

    $ # running the script directly works
    $ ./test.py
    /Users/tester/test.py

    $ # running the script with a .py named symlink works
    $ ln -s test.py link2test.py
    $ ./link2test.py
    /Users/tester/test.py
    $ rm link2test.py

    $ # running the script with a symlink without an extension works
    $ ln -s test.py link2test
    $ ./link2test
    /Users/tester/test.py
    $ rm link2test

    $ # running the script directly also works if it has no extension
    $ mv test.py testme
    $ ./testme
    /Users/tester/testme

    $ # running the extension-less script with a .py named symlink works
    $ ln -s testme link2test.py
    $ ./link2test.py
    /Users/tester/testme

----

automated tests, Github Actions, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.8.0 or newer

tested on recent linux with python 3.8, 3.9, 3.10, 3.11, pypy-3.9 - architectures: amd64

`100% code coverage <https://codeclimate.com/github/bitranox/lib_programname/test_coverage>`_, flake8 style checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://github.com/bitranox/lib_programname/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_programname/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_programname/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_programname/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=lib_programname.ipynb>`_

Usage
-----------

.. code-block:: python

    import lib_programname
    # this returns the fully resolved path to the launched python program
    path_to_program = lib_programname.get_path_executed_script()    # type: pathlib.Path

Usage from Commandline
------------------------

.. code-block::

   Usage: lib_programname [OPTIONS] COMMAND [ARGS]...

     get reliably the name of the executed script

   Options:
     --version                     Show the version and exit.
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

   Commands:
     info  get program informations

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block::

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade lib_programname


- to install the latest release from PyPi via pip, including test dependencies:

.. code-block::

    python -m pip install --upgrade lib_programname[test]

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/lib_programname.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_programname

    # for the latest development version :
    lib_programname @ git+https://github.com/bitranox/lib_programname.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version, including test dependencies from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/lib_programname.git
    $ cd lib_programname
    python -m pip install -e .[test]

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_programname.git
    $ cd lib_programname

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    cli_exit_tools
    lib_detect_testenv

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_programname/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

v2.0.8
---------
2023-07-13:
    - require minimum python 3.8
    - remove python 3.7 tests

v2.0.7
---------
2023-07-12:
    - also works now with symlinks
    - also works now with scripts and symlinks which do not have a ``py`` extension
    - clean ./tests/test_cli.py

v2.0.6
---------
2023-07-12:
    - introduce PEP517 packaging standard
    - introduce pyproject.toml build-system
    - remove mypy.ini
    - remove pytest.ini
    - remove setup.cfg
    - remove setup.py
    - remove .bettercodehub.yml
    - remove .travis.yml
    - update black config

v2.0.5
--------
2022-06-02: correct mypy type error

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


Version 1.1.4 as of 2020-07-31, see changelog_

=======================================================

lib_programname
===============

|travis_build| |license| |jupyter| |pypi|

|codecov| |better_code| |cc_maintain| |cc_issues| |cc_coverage| |snyk|


.. |travis_build| image:: https://img.shields.io/travis/bitranox/lib_programname/master.svg
   :target: https://travis-ci.org/bitranox/lib_programname

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/bitranox/lib_programname/master?filepath=lib_programname.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-programname?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_programname

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_programname
   :target: https://codecov.io/gh/bitranox/lib_programname

.. |better_code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_programname?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_programname

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_programname?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_programname/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_programname?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_programname/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_programname?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_programname/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://img.shields.io/snyk/vulnerabilities/github/bitranox/lib_programname
   :target: https://snyk.io/test/github/bitranox/lib_programname

Finding the name of the program from which a Python module is running can be trickier than it would seem at first, so lets make it damned easy.
This works under pycharm, pytest, pytest-docrunner, uwsgi, dreampie etc. correctly.

You might dive into Dough Hellmans `article <https://doughellmann.com/blog/2012/04/30/determining-the-name-of-a-process-from-python/>`_
about that issue.

.. code-block:: python

    $> python -m pip install lib_programname
    $> python
    >>> import lib_programname
    >>> path_to_program = lib_programname.get_path_executed_script()    # type: pathlib.Path

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.6.0 or newer

tested on linux "bionic" with python 3.6, 3.7, 3.8, 3.8-dev, pypy3

`100% code coverage <https://codecov.io/gh/bitranox/lib_programname>`_, codestyle checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://travis-ci.org/bitranox/lib_programname>`_, automatic daily builds and monitoring

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

.. code-block:: py

    import lib_programname
    # this returns the fully resolved path to the launched python program
    path_to_program = lib_programname.get_path_executed_script()    # type: pathlib.Path

Usage from Commandline
------------------------

.. code-block:: bash

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


.. code-block:: bash

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools
    python -m pip --upgrade wheel

- to install the latest release from PyPi via pip (recommended):

.. code-block:: bash

    # install latest release from PyPi
    python -m pip install --upgrade lib_programname

    # test latest release from PyPi without installing (can be skipped)
    python -m pip install lib_programname --install-option test

- to install the latest development version from github via pip:


.. code-block:: bash

    # normal install
    python -m pip install --upgrade git+https://github.com/bitranox/lib_programname.git

    # to test without installing (can be skipped)
    python -m pip install git+https://github.com/bitranox/lib_programname.git --install-option test

    # to install and upgrade all dependencies regardless of version number
    python -m pip install --upgrade git+https://github.com/bitranox/lib_programname.git --upgrade-strategy eager


- include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_programname

    # for the latest development version :
    lib_programname @ git+https://github.com/bitranox/lib_programname.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt



- to install the latest development version from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_programname.git
    $ cd lib_programname

    # to test without installing (can be skipped)
    python setup.py test

    # normal install
    python setup.py install

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
    cli_exit_tools @ git+https://github.com/bitranox/cli_exit_tools.git

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

tasks:
    - python 3.9 changes, __main__ should be now absolut path - check it


1.1.4
-------
2020-07-31: initial release


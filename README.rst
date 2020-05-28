lib_programname
===============

|Pypi Status| |license| |maintenance|

|Build Status| |Codecov Status| |Better Code| |code climate| |code climate coverage| |snyk security|

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License
.. |maintenance| image:: https://img.shields.io/maintenance/yes/2021.svg
.. |Build Status| image:: https://travis-ci.org/bitranox/lib_programname.svg?branch=master
   :target: https://travis-ci.org/bitranox/lib_programname
.. for the pypi status link note the dashes, not the underscore !
.. |Pypi Status| image:: https://badge.fury.io/py/lib-programname.svg
   :target: https://badge.fury.io/py/lib_programname
.. |Codecov Status| image:: https://codecov.io/gh/bitranox/lib_programname/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_programname
.. |Better Code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_programname?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_programname
.. |snyk security| image:: https://snyk.io/test/github/bitranox/lib_programname/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_programname
.. |code climate| image:: https://api.codeclimate.com/v1/badges/a177641a83f33aa78c9e/maintainability
   :target: https://codeclimate.com/github/bitranox/lib_programname/maintainability
   :alt: Maintainability
.. |code climate coverage| image:: https://api.codeclimate.com/v1/badges/a177641a83f33aa78c9e/test_coverage
   :target: https://codeclimate.com/github/bitranox/lib_programname/test_coverage
   :alt: Code Coverage

Finding the name of the program from which a Python module is running can be trickier than it would seem at first, so lets make it damned easy.
This works under pycharm, pytest, pytest-docrunner, uwsgi, dreampie etc. correctly.

You might dive into Dough Hellmans `article <https://doughellmann.com/blog/2012/04/30/determining-the-name-of-a-process-from-python/>`_
about that issue.

automated tests, Travis Matrix, Documentation, Badges for this Project are managed with `lib_travis_template <https://github
.com/bitranox/lib_travis_template>`_ - check it out

supports python 3.5-3.8, pypy3 and possibly other dialects.

`100% code coverage <https://codecov.io/gh/bitranox/lib_programname>`_, mypy static type checking, tested under `Linux, macOS, Windows and Wine <https://travis-ci
.org/bitranox/lib_programname>`_, automatic daily builds  and monitoring

----

- `Installation and Upgrade`_
- `Usage`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_programname/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_programname/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_programname/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Installation and Upgrade
------------------------

Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python3 -m pip --upgrade pip
    python3 -m pip --upgrade setuptools
    python3 -m pip --upgrade wheel


install latest version with pip (recommended):

.. code-block:: bash

    # upgrade all dependencies regardless of version number (PREFERRED)
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_programname.git --upgrade-strategy eager

    # test without installing (can be skipped)
    python3 -m pip install git+https://github.com/bitranox/lib_programname.git --install-option test

    # normal install
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_programname.git


install latest pypi Release (if there is any):

.. code-block:: bash

    # latest Release from pypi
    python3 -m pip install --upgrade lib_programname

    # test without installing (can be skipped)
    python3 -m pip install lib_programname --install-option test

    # normal install
    python3 -m pip install --upgrade lib_programname



include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi (if any):
    lib_programname
    # for the latest Development Version :
    lib_programname @ git+https://github.com/bitranox/lib_programname.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python3 -m pip install --upgrade -r /<path>/requirements.txt


Install from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_programname.git
    $ cd lib_programname

    # test without installing (can be skipped)
    python3 setup.py test

    # normal install
    python3 setup.py install


via makefile:

if You are on linux, makefiles are a very convenient way to install. Here we can do much more, like installing virtual environment, clean caches and so on.
This is still in development and not recommended / working at the moment:

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

Usage
-----------

.. code-block:: py

    import lib_programname
    # this returns the fully resolved path to the launched python program
    path_to_program = lib_programname.get_programname_fullpath()    # type: pathlib.Path

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    docopt

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"
- thanks to Dough Hellman for his `article <https://doughellmann.com/blog/2012/04/30/determining-the-name-of-a-process-from-python/>`_ about that issue

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

0.1.0
-----
2020-05-15: Initial public release


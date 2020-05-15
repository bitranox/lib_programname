lib_programname
===============

|Pypi Status| |license| |maintenance|

|Build Status| |Codecov Status| |Better Code| |code climate| |snyk security|

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
.. |code climate| image:: https://api.codeclimate.com/v1/badges/4a90a2679cbe3c2989d4/maintainability
   :target: https://codeclimate.com/github/bitranox/lib_programname/maintainability
   :alt: Maintainability

Finding the name of the program from which a Python module is running can be trickier than it would seem at first

supports python 3.8 and possibly other dialects.

`100% code coverage <https://codecov.io/gh/bitranox/lib_programname>`_, mypy static type checking, tested under `Linux, OsX, Windows and Wine <https://travis-ci.org/bitranox/lib_programname>`_, automatic daily builds  and monitoring

----

- `Installation and Upgrade`_
- `Basic Usage`_
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

From source code:

.. code-block:: bash

    # normal install
    python setup.py install
    # test without installing
    python setup.py test

via pip latest Release:

.. code-block:: bash

    # latest Release from pypi
    pip install lib_programname

    # test without installing
    pip install lib_programname --install-option test

via pip latest Development Version:

.. code-block:: bash

    # upgrade all dependencies regardless of version number (PREFERRED)
    pip install --upgrade git+https://github.com/bitranox/lib_programname.git --upgrade-strategy eager
    # normal install
    pip install --upgrade git+https://github.com/bitranox/lib_programname.git
    # test without installing
    pip install git+https://github.com/bitranox/lib_programname.git --install-option test

via requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release:
    lib_programname
    # for the latest Development Version :
    git+https://github.com/bitranox/lib_programname.git

    # to install and upgrade all modules mentioned in requirements.txt:
    pip install --upgrade -r /<path>/requirements.txt

via python:

.. code-block:: python

    # for the latest Release
    python -m pip install upgrade lib_programname

    # for the latest Development Version
    python -m pip install upgrade git+https://github.com/bitranox/lib_programname.git

Basic Usage
-----------

.. code-block:: py

    import lib_programname
    # this returns the fully resolved path to the launched python program
    path_to_program = lib_programname.get_programname_fullpath()    # type: pathlib.Path

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Test Requirements
    ## following Requirements will be installed temporarily for
    ## "setup.py install test" or "pip install <package> --install-option test"
    docopt
    typing ; python_version < "3.5"
    pathlib; python_version < "3.4"
    mypy ; platform_python_implementation != "PyPy" and python_version >= "3.5"
    pytest
    pytest-pep8 ; python_version < "3.5"
    pytest-pycodestyle ; python_version >= "3.5"
    pytest-mypy ; platform_python_implementation != "PyPy" and python_version >= "3.5"
    pytest-runner

    ## Project Requirements

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

0.0.1
-----
2020-05-15: Initial public release


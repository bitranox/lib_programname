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


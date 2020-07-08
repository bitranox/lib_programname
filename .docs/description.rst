Finding the name of the program from which a Python module is running can be trickier than it would seem at first, so lets make it damned easy.
This works under pycharm, pytest, pytest-docrunner, uwsgi, dreampie etc. correctly.

You might dive into Dough Hellmans `article <https://doughellmann.com/blog/2012/04/30/determining-the-name-of-a-process-from-python/>`_
about that issue.

.. code-block:: python

    $> python -m pip install lib_programname
    $> python
    >>> import lib_programname
    >>> path_to_program = lib_programname.get_path_executed_script()    # type: pathlib.Path

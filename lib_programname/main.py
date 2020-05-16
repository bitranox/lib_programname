# Finding the name of the program from which a Python module is
# running can be trickier than it would seem at first
# see : https://doughellmann.com/blog/2012/04/30/determining-the-name-of-a-process-from-python/

# stdlib
import inspect
import __main__   # type: ignore
import pathlib
import sys

empty_path = pathlib.Path()


def get_programname_fullpath() -> pathlib.Path:
    """ getting the full path of the program from which a Python module is running  """

    # try to get it from __main__.__file__ - does not work under pytest, doctest
    path_candidate = get_fullpath_from_main_file()
    if path_candidate != empty_path:
        return path_candidate

    # try to get it from sys_argv - does not work when loaded from uwsgi, works in eclipse and pydev
    path_candidate = get_fullpath_from_sys_argv()
    if path_candidate != empty_path:
        return path_candidate

    # try to get it from stack, works under dreampie
    path_candidate = get_fullpath_from_stack()
    if path_candidate != empty_path:
        return path_candidate

    raise RuntimeError('can not determine the path of the launched program')


def get_fullpath_from_main_file() -> pathlib.Path:
    """ try to get it from __main__.__file__ - does not work under pytest, doctest

    >>> if is_doctest_running(): assert get_fullpath_from_main_file() == empty_path
    >>> if is_setup_test_running(): assert get_fullpath_from_main_file() != empty_path

    """
    if not hasattr(sys.modules['__main__'], '__file__'):
        return empty_path

    arg_string = __main__.__file__
    valid_executable_path = get_valid_executable_path_or_false(arg_string)
    return valid_executable_path


def get_fullpath_from_sys_argv() -> pathlib.Path:
    """ try to get it from sys_argv - does not work when loaded from uwsgi, works in eclipse and pydev

    >>> if (not is_pytest_main_in_sys_argv()) and is_doctest_running(): assert get_fullpath_from_sys_argv() == pathlib.Path(__file__).resolve()
    >>> if not is_doctest_running(): assert get_fullpath_from_sys_argv() != pathlib.Path()
    """

    for arg_string in sys.argv:
        valid_executable_path = get_valid_executable_path_or_false(arg_string)
        if valid_executable_path != empty_path:
            return valid_executable_path
    return empty_path


def get_fullpath_from_stack() -> pathlib.Path:
    """ try to get it from stack, works under dreampie

    >>> assert get_fullpath_from_stack() == pathlib.Path(__file__).resolve()

    """

    levels_back = 0
    while True:
        try:
            arg_string = inspect.stack()[levels_back][1]
            valid_executable_path = get_valid_executable_path_or_false(arg_string)
            if valid_executable_path != empty_path:
                return valid_executable_path
            levels_back += 1
        except IndexError:
            break
    return empty_path


def get_valid_executable_path_or_false(arg_string: str) -> pathlib.Path:
    """
    >>> if is_doctest_running(): assert get_valid_executable_path_or_false(__main__.__file__) == empty_path
    >>> assert get_valid_executable_path_or_false(__file__) == pathlib.Path(__file__).resolve()
    """

    if is_doctest_in_arg_string(arg_string):
        return empty_path

    arg_string = remove_doctest_and_docrunner_parameters(arg_string)
    arg_string = add_python_extension_if_not_there(arg_string)
    path = pathlib.Path(arg_string).resolve()
    if path.is_file():
        return path
    else:
        return empty_path


def remove_doctest_and_docrunner_parameters(arg_string: str) -> str:
    """
    >>> # Setup
    >>> arg_string_with_parameter = __file__ + '::::::some docrunner parameter'
    >>> arg_string_without_parameter = __file__

    >>> # Test with and without docrunner parameters
    >>> assert remove_doctest_and_docrunner_parameters(arg_string_with_parameter) == __file__
    >>> assert remove_doctest_and_docrunner_parameters(arg_string_without_parameter) == __file__
    """
    path = arg_string.split('::', 1)[0]
    return path


def add_python_extension_if_not_there(arg_string: str) -> str:
    """
    >>> # Setup
    >>> arg_string_with_py = __file__
    >>> arg_string_without_py = __file__.rsplit('.py',1)[0]

    >>> # Test with and without .py suffix
    >>> assert add_python_extension_if_not_there(arg_string_with_py) == __file__
    >>> assert add_python_extension_if_not_there(arg_string_without_py) == __file__

    """

    if not arg_string.endswith('.py'):
        arg_string = arg_string + '.py'
    return arg_string


def is_doctest_running() -> bool:
    """
    >>> if not is_setup_test_running(): assert is_doctest_running() == True
    """
    for argv in sys.argv:
        if is_doctest_in_arg_string(argv):
            return True
    return False


def is_doctest_in_arg_string(arg_string: str) -> bool:
    """
    >>> assert is_doctest_in_arg_string('test') == False
    >>> assert is_doctest_in_arg_string('test/docrunner.py::::test')
    >>> assert is_doctest_in_arg_string('test/pytest.py::::test')
    """
    arg_string = arg_string.replace('\\', '/')
    if ('docrunner.py' in arg_string) or ('pytest.py' in arg_string) or ('/pytest/__main__.py' in arg_string):
        return True
    else:
        return False


def is_pytest_main_in_sys_argv() -> bool:
    for arg_string in sys.argv:
        arg_string = arg_string.replace('\\', '/')
        if '/pytest/__main__.py' in arg_string:
            return True
    return False


def is_setup_test_running() -> bool:
    """ if 'setup.py test' was launched """
    for arg_string in sys.argv:
        if 'setup.py' in arg_string:
            return True
    return False

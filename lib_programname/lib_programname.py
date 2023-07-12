# STDLIB
import inspect
import __main__  # noqa
import pathlib
import sys

# OWN
import lib_detect_testenv


__all__ = ["get_path_executed_script"]

empty_path = pathlib.Path()


def get_path_executed_script() -> pathlib.Path:
    """
    getting the full path of the program from which a Python module is running

    >>> ### TEST get it via __main__.__file__
    >>> # Setup
    >>> # force __main__.__file__ valid
    >>> save_main_file = str(__main__.__file__)
    >>> __main__.__file__ = __file__

    >>> # Test via __main__.__file__
    >>> assert get_path_executed_script() == pathlib.Path(__file__).resolve()


    >>> ### TEST get it via sys.argv
    >>> # Setup
    >>> # force __main__.__file__ invalid
    >>> __main__.__file__ = str((pathlib.Path(__file__).parent / 'invalid_file.py'))

    >>> # force sys.argv valid
    >>> save_sys_argv = list(sys.argv)
    >>> valid_path = str((pathlib.Path(__file__).resolve()))
    >>> sys.argv = [valid_path]

    >>> # Test via sys.argv
    >>> assert get_path_executed_script() == pathlib.Path(__file__).resolve()


    >>> ### TEST get it via stack
    >>> # Setup
    >>> # force sys.argv invalid
    >>> invalid_path = str((pathlib.Path(__file__).parent / 'invalid_file.py'))
    >>> sys.argv = [invalid_path]


    >>> assert get_path_executed_script()

    >>> # teardown
    >>> __main__.__file__ = save_main_file
    >>> sys.argv = list(save_sys_argv)

    """

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

    raise RuntimeError("can not determine the path of the launched program")  # pragma: no cover


def get_fullpath_from_main_file() -> pathlib.Path:
    """try to get it from __main__.__file__ - does not work under pytest, doctest

    >>> if lib_detect_testenv.is_doctest_active(): assert get_fullpath_from_main_file() == empty_path
    >>> if lib_detect_testenv.is_setup_active(): assert get_fullpath_from_main_file() != empty_path

    >>> # test no attrib __main__.__file__
    >>> save_main_file = str(__main__.__file__)
    >>> delattr(__main__, '__file__')
    >>> assert get_fullpath_from_main_file() == empty_path
    >>> setattr(__main__, '__file__', save_main_file)

    """
    if not hasattr(sys.modules["__main__"], "__file__"):
        print('from main')
        return empty_path

    arg_string = str(sys.modules["__main__"].__file__)
    valid_executable_path = get_valid_executable_path_or_empty_path(arg_string)
    return valid_executable_path


def get_fullpath_from_sys_argv() -> pathlib.Path:
    """try to get it from sys_argv - does not work when loaded from uwsgi, works in eclipse and pydev

    >>> # if (not is_pytest_main_in_sys_argv()) and is_doctest_running(): assert get_fullpath_from_sys_argv() == pathlib.Path(__file__).resolve()
    >>> if lib_detect_testenv.is_doctest_active() and not lib_detect_testenv.is_pytest_active():
    ...     assert get_fullpath_from_sys_argv() == pathlib.Path(__file__).resolve()
    >>> if not lib_detect_testenv.is_doctest_active(): assert get_fullpath_from_sys_argv() != pathlib.Path()

    >>> # force test invalid sys.path
    >>> save_sys_argv = list(sys.argv)
    >>> invalid_path = str((pathlib.Path(__file__).parent / 'invalid_file.py'))
    >>> sys.argv = [invalid_path]
    >>> assert get_fullpath_from_sys_argv() == pathlib.Path()
    >>> sys.argv = list(save_sys_argv)

    >>> # force test valid sys.path
    >>> save_sys_path = list(sys.argv)
    >>> valid_path = str((pathlib.Path(__file__).resolve()))
    >>> sys.argv = [valid_path]
    >>> assert get_fullpath_from_sys_argv() == pathlib.Path(valid_path)
    >>> sys.argv = list(save_sys_argv)


    """

    for arg_string in sys.argv:
        valid_executable_path = get_valid_executable_path_or_empty_path(arg_string)
        if valid_executable_path != empty_path:
            return valid_executable_path
    return empty_path


def get_fullpath_from_stack() -> pathlib.Path:
    """try to get it from stack, works under dreampie

    >>> assert get_fullpath_from_stack() == pathlib.Path(__file__).resolve()

    """

    levels_back = 0
    while True:
        try:
            arg_string = inspect.stack()[levels_back][1]
            valid_executable_path = get_valid_executable_path_or_empty_path(arg_string)
            if valid_executable_path != empty_path:  # pragma: no cover     # its hard to tamper around with the stack, therefore we dont cover it
                return valid_executable_path
            levels_back += 1  # pragma: no cover
        except IndexError:  # pragma: no cover
            break  # pragma: no cover
    return empty_path  # pragma: no cover


def get_valid_executable_path_or_empty_path(arg_string: str) -> pathlib.Path:
    """
    >>> ## normal execution
    >>> assert get_valid_executable_path_or_empty_path(__file__) == pathlib.Path(__file__).resolve()
    >>> # docrunner.py or doctest.py active
    >>> if lib_detect_testenv.is_doctest_active(): assert get_valid_executable_path_or_empty_path(__main__.__file__) == empty_path
    >>> # doctest.py active
    >>> assert get_valid_executable_path_or_empty_path("doctest.py") == empty_path
    """

    # if is_doctest_in_arg_string(arg_string):
    if lib_detect_testenv.is_doctest_active(arg_string):
        return empty_path

    arg_string = remove_doctest_and_docrunner_parameters(arg_string)
    # arg_string = add_python_extension_if_not_there(arg_string)
    path = pathlib.Path(arg_string)
    if path.is_file():
        path = path.resolve()
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
    path = arg_string.split("::", 1)[0]
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

    if not arg_string.endswith(".py"):
        arg_string = arg_string + ".py"
    return arg_string


if __name__ == "__main__":
    print("this is a library only, the executable is named lib_programname_cli.py")

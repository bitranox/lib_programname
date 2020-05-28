"""
Usage:  lib_programname (-h | -v | -i)

    -h, --help          show help
    -v, --version       show version
    -i, --info          show Info

Finding the name of the program from which a Python module is running can be trickier than it would seem at first
see : https://doughellmann.com/blog/2012/04/30/determining-the-name-of-a-process-from-python/

this module exposes no other useful functions to the commandline

"""
# docopt syntax see : http://docopt.org/


# STDLIB
import inspect
import __main__   # type: ignore
import pathlib
import sys
from typing import Dict, Union

# EXT
from docopt import docopt           # type: ignore

# PROJ
try:
    from . import __init__conf__
except ImportError:                 # pragma: no cover
    # imports for doctest
    import __init__conf__           # type: ignore  # pragma: no cover


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

    >>> # test no attrib __main__.__file__
    >>> save_main_file = str(__main__.__file__)
    >>> delattr(__main__, '__file__')
    >>> assert get_fullpath_from_main_file() == empty_path
    >>> setattr(__main__, '__file__', save_main_file)

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

    >>> # force test invalid sys.path
    >>> save_sys_argv = list(sys.argv)
    >>> invalid_path = str((pathlib.Path(__file__).parent / 'invalid_file.py'))  # .resolve() seems not to work on a non existing file in python 3.5
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
    path = pathlib.Path(arg_string)
    if path.is_file():
        path = path.resolve()   # .resolve does not work on a non existing file in python 3.5
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

    >>> # fore test doctest is not running
    >>> save_sys_argv = list(sys.argv)
    >>> invalid_path = str((pathlib.Path(__file__).parent / 'invalid_file.py'))  # .resolve does not work on a non existing file in python 3.5
    >>> sys.argv = [invalid_path]
    >>> assert not is_doctest_running()
    >>> sys.argv = list(save_sys_argv)

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
    """
    >>> # force pytest is running
    >>> save_sys_argv = list(sys.argv)
    >>> fake_pytest_path = str((pathlib.Path(__file__).parent / 'pytest/__main__.py').resolve())
    >>> sys.argv = [fake_pytest_path]
    >>> assert is_pytest_main_in_sys_argv()
    >>> sys.argv = list(save_sys_argv)

    >>> # force pytest is not running
    >>> save_sys_argv = list(sys.argv)
    >>> invalid_path = str((pathlib.Path(__file__).parent / 'invalid_file.py'))   # .resolve does not work on a non existing file in python 3.5
    >>> sys.argv = [invalid_path]
    >>> assert not is_pytest_main_in_sys_argv()
    >>> sys.argv = list(save_sys_argv)
    """
    for arg_string in sys.argv:
        arg_string = arg_string.replace('\\', '/')
        if '/pytest/__main__.py' in arg_string:
            return True
    return False


def is_setup_test_running() -> bool:
    """ if 'setup.py test' was launched

    >>> # force setup.py is running
    >>> save_sys_argv = list(sys.argv)
    >>> fake_setup_path = str((pathlib.Path(__file__).parent / 'setup.py').resolve())
    >>> sys.argv = [fake_setup_path]
    >>> assert is_setup_test_running()
    >>> sys.argv = list(save_sys_argv)

    >>> # force setup.py is not running
    >>> save_sys_argv = list(sys.argv)
    >>> invalid_path = str((pathlib.Path(__file__).parent / 'invalid_file.py'))     # .resolve does not work on a non existing file in python 3.5
    >>> sys.argv = [invalid_path]
    >>> assert not is_setup_test_running()
    >>> sys.argv = list(save_sys_argv)

    """

    for arg_string in sys.argv:
        if 'setup.py' in arg_string:
            return True
    return False


# we might import this module and call main from another program and pass docopt args manually
def main(docopt_args: Dict[str, Union[bool, str]]) -> None:
    """
    >>> docopt_args = dict()
    >>> docopt_args['--version'] = True
    >>> docopt_args['--info'] = False
    >>> main(docopt_args)   # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    version: ...


    >>> docopt_args['--version'] = False
    >>> docopt_args['--info'] = True
    >>> main(docopt_args)   # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    information for ...

    >>> docopt_args['--version'] = False
    >>> docopt_args['--info'] = False
    >>> main(docopt_args)


    """
    if docopt_args['--version']:
        __init__conf__.print_version()
    elif docopt_args['--info']:
        __init__conf__.print_info()


# entry point via commandline
def main_commandline() -> None:
    """
    >>> main_commandline()  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    docopt.DocoptExit: ...

    """
    docopt_args = docopt(__doc__)
    main(docopt_args)       # pragma: no cover


# entry point if main
if __name__ == '__main__':
    main_commandline()

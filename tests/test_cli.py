# STDLIB
import logging
import pathlib
import subprocess
import sys

logger = logging.getLogger()
package_dir = "lib_programname"
cli_filename = "lib_programname_cli.py"


def call_cli_command(cli_command: str, commandline_args: str) -> bool:
    command = " ".join([cli_command, commandline_args]).strip()
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        return False
    return True


def test_cli_commands() -> None:
    cli_command = " ".join([sys.executable, str(pathlib.Path(__file__).resolve().parent.parent / package_dir / cli_filename)]).strip()
    assert not call_cli_command(cli_command, "--unknown_option")
    assert call_cli_command(cli_command, "--version")
    assert call_cli_command(cli_command, "-h")
    assert call_cli_command(cli_command, "info")
    assert call_cli_command(cli_command, "--traceback info")


def execute_script(script_name: str) -> str:
    """
    >>> # shebang without extension
    >>> set_shebang("script_without_extension")
    >>> execute_script("script_without_extension")
    '/.../lib_programname/tests/script_without_extension'

    >>> # shebang with extension
    >>> set_shebang("script_with_extension.py")
    >>> execute_script("script_with_extension.py")
    '/.../lib_programname/tests/script_with_extension.py'

    """
    # cli_command = " ".join([sys.executable, get_str_path_to_script(script_name)]).strip()
    cli_command = get_str_path_to_script(script_name)
    result = subprocess.run(cli_command, shell=True, check=True, capture_output=True).stdout.decode('utf-8').strip()
    return result


def get_str_path_to_script(script_name: str) -> str:
    """
    >>> get_str_path_to_script('test_script')
    '/.../lib_programname/tests/test_script'

    """
    path_to_script = get_test_directory() / script_name
    str_path_to_script = str(path_to_script).strip()
    return str_path_to_script


def get_test_directory() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent


def set_shebang(script_name: str) -> str:
    """
    >>> set_shebang("script_with_extension.py")

    """
    my_txt = (get_test_directory() / script_name).read_text()
    my_txt = my_txt.replace('/usr/bin/python3', str(sys.executable))
    (get_test_directory() / script_name).write_text(my_txt)
    return my_txt

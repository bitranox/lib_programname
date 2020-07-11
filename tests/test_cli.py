# EXT
from click.testing import CliRunner

# OWN
import lib_programname.lib_programname_cli as lib_programname_cli

runner = CliRunner()
runner.invoke(lib_programname_cli.cli_main, ['--version'])
runner.invoke(lib_programname_cli.cli_main, ['-h'])
runner.invoke(lib_programname_cli.cli_main, ['info'])

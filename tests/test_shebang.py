#!python
import pathlib
import lib_programname
# this returns the fully resolved path to the launched python program
path_to_program = lib_programname.get_path_executed_script()  # type: pathlib.Path
print(path_to_program)

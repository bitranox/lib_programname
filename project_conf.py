# single point for all configuration of the project

# stdlib
import pathlib
from typing import List, Dict

package_name = 'lib_programname'  # type: str
version = '0.0.1'
codeclimate_link_hash = "a177641a83f33aa78c9e"                                             # for lib_programname
cc_test_reporter_id = 'a745068413ec369527ed6cf0aaabc344894fbad87231f5a7649ffb929c19e0ce'   # codeclimate coverage id for lib_programname

# include package data files
# package_data = {package_name: ['some_file_to_include.txt']}
package_data = dict()

# pypi_password
# to create the secret :
# cd /<repository>
# travis encrypt -r bitranox/lib_parameter pypi_password=*****
# copy and paste the encrypted password here
travis_secure = 'none'      # secure

# Entry Points Example :
# need to create __main__.py:
#   from . import <module_name>
#   <module_name>.main()
shell_command = package_name
src_dir = package_name
module_name = package_name
init_config_title = package_name
init_config_name = package_name

# entry_points = {'console_scripts': ['{shell_command} = {src_dir}.{module_name}:main'
#                 .format(shell_command=shell_command, src_dir=src_dir, module_name=module_name)]}  # type: Dict[str, List[str]]

entry_points = dict()  # type: Dict[str, List[str]]

author = 'Robert Nowotny'
author_email = 'rnowotny1966@gmail.com'
github_account = 'bitranox'


description = package_name  # short description - should be entered here
long_description = package_name  # will be overwritten with the content of README.rst if exists
packages = [package_name]
url = 'https://github.com/bitranox/{package_name}'.format(package_name=package_name)

CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Software Development :: Libraries :: Python Modules']


def create_init_config_file() -> None:
    path_version_py = pathlib.Path(__file__).parent / src_dir / 'init_config.py'
    with open(path_version_py, 'w') as f_version_py:
        lines = ["version = '{}'\n".format(version),
                 "title = '{}'\n".format(init_config_title),
                 "name = '{}'\n".format(init_config_name)]
        f_version_py.writelines(lines)


if __name__ == '__main__':
    create_init_config_file()

    # create readme.rst
    import build_docs
    build_docs_args = dict()
    build_docs_args['<TRAVIS_REPO_SLUG>'] = '{}/{}'.format(github_account, package_name)
    build_docs.main(build_docs_args)

    # create Travis File from Template

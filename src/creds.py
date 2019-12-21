"""creds.py
"""
__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# built-in Python Modules
import os
from sys import stdout
import getpass

# external Python Modules
try:
    import keyring
    # imported keyring succesfully
    keyring_import = True
except ImportError as error:
    # log error
    stdout.write(error)
    # we set keyring import to False
    keyring_import = False


def _set_username(option):
    pass


def _set_password(option):
    pass


def _get_username(option):
    pass


def _get_password(option):
    pass

"""creds.py
"""
__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# built-in Python Modules
import os
import sys
import getpass

# external Python Modules
try:
    import keyring
    # imported keyring succesfully
    keyring_import = True
except ImportError as error:
    # log error
    sys.stdout.write(str(error))
    # we set keyring import to False
    keyring_import = False


def _set_username(option=None):
    pass


def _set_password(option=None):
    pass


def _get_username():
    pass


def _get_password():
    pass

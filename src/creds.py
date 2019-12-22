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


def _set_username(key, git):
    keyring.set_password('git_username', key, git)


def _set_password(git, pw):
    keyring.set_password('git_password', git, pw)


def _get_username(key):
    return keyring.get_password('git_username', key)


def _get_password(git):
    return keyring.get_password('git_password', git)


def _check_username(key):
    if _get_username(key):
        return True
    else:
        return False


def _check_password(password):
    if _get_password(password):
        return True
    else:
        return False


def _reset_username(username):
    pass


def _reset_password(password):
    pass


def _create_creds(key, username, password):
    _set_username(key, username)
    _set_password(username, password)


def valid_credentials(username, password):
    try:
        g = Github(username, password=password)
        user = g.get_user().login
        return True
    except:
        return False

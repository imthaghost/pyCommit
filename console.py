"""console.py
"""
__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# built-in Python Modules
from pprint import pprint
import random
import regex

# local Python Modules
from src.creds import _create_creds, _get_password, _get_username, _check_password, _check_username, valid_credentials
from src.pycommit import pyCommit
from src.art import git

# local Python Docs
from src.creds import __doc__ as credential_doc
from src.mon import __doc__ as daemon_doc
from src.death import __doc__ as death_doc
from src.pycommit import __doc__ as pycommit_doc

# external Python Modules
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from colorama import Fore, Back, Style
import colorama
import emoji


# initilize colorama
colorama.init()


def banner_logo():
    # banner colors
    banner_colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
                     Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.BLUE, Fore.CYAN]
    # banner
    banner = Style.BRIGHT + random.choice(banner_colors) + git + Fore.RESET
    print(banner)
    print('\n')


def welcome():
    welcome_emoji_list = ['\U0001F918',
                          '\U0001F44B', '\U0001F5A4', '\U0001F47D', '\U0001F642', '\U0001F601', '\U0001F603', '\U0001F435', '\U0001F40D',
                          '\U0001F996']
    print('       Hi, welcome to pyCommit' +
          emoji.emojize(random.choice(welcome_emoji_list)) + '\n')


def successful_login(username, password):
    pass


class NumberValidator(Validator):
    """"""

    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end


class DateValidator(Validator):
    """"""

    def validate(self, document):
        ok = regex.match(
            '^(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid date',
                cursor_position=len(document.text))  # Move cursor to end


class CredsValidator(Validator):
    def validate(self, document):
        ok = successful_login()


def login(key, username, password):
    reset = [
        {
            'type': 'input',
            'name': 'username',
            'message': 'Whats your github username'
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'Whats your github password'
        }
    ]
    reset_style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    if valid_credentials(username, password):
        print('\n')
        # print success message
        print(Fore.GREEN + 'Successful Login' + Fore.RESET)
        print('\n')
        # return True
        return True
    else:
        # print failed message
        print(Fore.RED + 'Invalid credentials' + Fore.RESET)
        # ask the user for new credentials
        new_credentials = prompt(reset, style=reset_style)
        # set the new credentials
        _create_creds(
            key, new_credentials['username'], new_credentials['password'])
        # ask for home dashboard
        home()


def home():
    # key will be used to get github username
    key = 'wall-e'
    # try logging in otehrwise we will get the users credentials
    login(key, _get_username(key), _get_password(_get_username(key)))


def commit_prompt():
    # prompt styling
    commit_style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })
    # create questions to ask user
    questions = [
        {
            'type': 'list',
            'name': 'server',
            'message': 'Where should this be executed',
            'choices': ['Local Machine', 'Web-Server'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'repo_type',
            'message': 'Existing or New Repository',
            'choices': ['Existing', 'New'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'repo_status',
            'message': 'Private or public',
            'choices': ['Private', 'Public'],
            'filter': lambda val: val.lower(),
            'when': lambda answers: answers['repo_type'] == 'new'
        },
        {
            'type': 'input',
            'name': 'repo_name',
            'message': 'What is the repos name',
            'filter': lambda val: val.lower(),
            'when': lambda answers: answers['repo_type'] == 'existing'
        },
        # {
        #     'type': 'input',
        #     'name': 'start',
        #     'message': 'Start Date - format(mm/dd/yyyy)',
        #     'validate': DateValidator
        # },
        # {
        #     'type': 'input',
        #     'name': 'end',
        #     'message': 'End Date - format(mm/dd/yyyy)',
        #     'validate': DateValidator
        # },
        {
            'type': 'input',
            'name': 'quantity',
            'message': 'How many commits do you want?',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'input',
            'name': 'comments',
            'message': 'Any comments on your experience?',
            'default': 'Nope, all good!'
        },
        {
            'type': 'list',
            'name': 'ending',
            'message': 'Thanks for leaving a comment!',
            'when': lambda answers: answers['comments'] != 'Nope, all good!'
        }
    ]
    answers = prompt(questions, style=commit_style)
    pprint(answers)
    # if the user wants to run the daemon locally then we use keyring process
    if 'local' in answers['server']:
        print('\n')
        print('creating daemon..')

    else:
        print('Server not up yet .-.')


def main():
    banner_logo()
    welcome()
    home()
    commit_prompt()


if __name__ == "__main__":
    main()

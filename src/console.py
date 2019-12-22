"""console.py
"""
__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# built-in Python Modules
from pprint import pprint
import regex

# local Python Modules
from art import git as banner

# external Python Modules
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import colorama
from colorama import Fore, Back, Style

# initilize
colorama.init()
# promt styling
style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


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


print(Fore.LIGHTCYAN_EX)
print(banner + '\n')
print('Hi, welcome to pyCommit' + '\n')
print(Style.RESET_ALL)
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
    {
        'type': 'input',
        'name': 'start',
        'message': 'Start Date - format(mm/dd/yyyy)',
        'validate': DateValidator
    },
    {
        'type': 'input',
        'name': 'end',
        'message': 'End Date - format(mm/dd/yyyy)',
        'validate': DateValidator
    },
    {
        'type': 'input',
        'name': 'username',
        'message': 'Whats your github username'
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'Whats your github password'
    },

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


def py_console():
    pass


if __name__ == "__main__":
    answers = prompt(questions, style=style)
    # pprint(answers)

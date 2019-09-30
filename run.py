from errors import *  # import all defined erros
import sys
import os
import time     # lets time the processess
# multiprocessing library
from multiprocessing import Process, ProcessError, Pool, Queue, Value, Array


if '3' in sys.version[0]:
    sys.stdout.write(
        '\x1b[1;32m' + '[+] Running Python version: ' + sys.version + '\x1b[0m' + '\n')
else:

    raise version_error(
        'Run application with latest version of python', sys.version)

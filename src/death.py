"""Kill/Terminate Disk And Execution MONitor Process (Daemon)

References:
   1) Advanced Programming in the Unix Environment: W. Richard Stevens
   2) Unix Programming Frequently Asked Questions:
         http://www.erlenstar.demon.co.uk/unix/faq_toc.html
"""
__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'

# Standard Python modules.
import os               # Miscellaneous OS interfaces.
import sys              # System-specific parameters and functions.
import daemon           # Standard daemon process library: PEP 3143

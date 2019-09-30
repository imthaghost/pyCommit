import sys
import os
from multiprocessing import ProcessError


class commit_error(Exception):
    """
    description:

    """

    def __init__(self, message):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


class push_error(Exception):
    """
    description:

    """

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


class add_error(Exception):
    """
    description:

    """

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


class version_error(Exception):
    """
    description:
    """

    def __init__(self, text, version):
        """
        description:
        """
        super(Exception, self).__init__(text)
        self._version = str(sys.version)

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, val):
        self._version = val

    def __repr__(self):
        return "VersionError{!r}, {!r}".format(self.args[0], self._version)

    def __str__(self):
        return "'{}' for version {}".format(self.args[0], self._version)


class child_process_failed(ProcessError):
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(Self):
        pass

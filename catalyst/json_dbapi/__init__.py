import json, datetime, os

from .sqlparser import parse


def Date(year, month, day):
    raise NotImplementedError()


def Timestamp(hour, minute, second):
    raise NotImplementedError()


def Timestamp(year, month, day, hour, minute, second):
    raise NotImplementedError()


def DateFromTicks(ticks):
    raise NotImplementedError()


def TimeFromTicks(ticks):
    raise NotImplementedError()


def TimeStampFromTicks(ticks):
    raise NotImplementedError()


def Binary(value):
    return bytes(value)


STRING = str
BINARY = bytes
NUMBER = float
DATETIME = datetime.datetime
ROWID = int


class JsonDBAPICursor(object):
    def __init__(self, owner):
        self.owner = owner
        self.arraysize = 1
        self._results = None

    @property
    def description(self):
        raise NotImplementedError()

    @property
    def rowcount(self):
        raise NotImplementedError()

    def close(self):
        pass

    def execute(self, operation, parameters=None):
        stmt = parse(operation)
        ret, self._results = stmt.execute(parameters)
        raise Exception("Operation '%s' not supported" % operation)

    def executemany(self, operation, parameter_seq):
        raise NotImplementedError()

    def fetchone(self):
        raise NotImplementedError()

    def fetchmany(self, size=None):
        if size is None:
            size = self.arraysize
        raise NotImplementedError()

    def fetchall(self):
        raise NotImplementedError()

    def setinputsizes(self, sizes):
        pass

    def setoutputsize(self, size, column=None):
        pass


class JsonDBAPIConnection(object):
    def __init__(self, filename):
        self.filename = filename
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                self.j = json.load(f)
        else:
            self.j = {}

    def close(self):
        pass

    def commit(self):
        raise NotImplementedError()

    def cursor(self):
        return JsonDBAPICursor(self)

    def rollback(self):
        pass


apilevel = "1.0"

threadsafety = 0

paramstyle = "format"


def connect(filename):
    return JsonDBAPIConnection(filename)

Error = Exception

DatabaseError = Exception
"""Stub file for the 'datetime' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, Undefined, GenericType

max = Undefined(object)
min = Undefined(object)
resolution = Undefined(object)

class date(object):
    def __format__(a) -> unicode:
        raise ValueError()
    def __reduce__() -> tuple: ...
    def ctime() -> str: ...
    def fromordinal(a: int) -> object:
        raise ValueError()
    def fromtimestamp(a: float) -> object: ...
    def isocalendar() -> tuple: ...
    def isoformat() -> str: ...
    def isoweekday() -> int: ...
    def replace(*args, **kwargs) -> object: ...
    def strftime(format) -> object: ...
    def timetuple() -> object: ...
    def today() -> object: ...
    def toordinal() -> int: ...
    def weekday() -> int: ...

class datetime(object):
    def __reduce__() -> tuple: ...
    def astimezone(tz) -> object:
        raise ValueError()
    def combine(date, time) -> object: ...
    def ctime() -> str: ...
    def date() -> object: ...
    def dst() -> object: ...
    def fromtimestamp(timestamp: float, *args, **kwargs) -> object: ...
    def isoformat(*args, **kwargs) -> str: ...
    def now(*args, **kwargs) -> object: ...
    def replace(*args, **kwargs) -> object: ...
    def strptime(a: str, b: str) -> object:
        raise ValueError()
    def time() -> object: ...
    def timetuple() -> object: ...
    def timetz() -> object: ...
    def tzname() -> object: ...
    def utcfromtimestamp(a: float) -> object: ...
    def utcnow() -> object: ...
    def utcoffset() -> object: ...
    def utctimetuple() -> object:
        raise OverflowError()

class time(object):
    def __format__(a) -> unicode:
        raise ValueError()
    def __reduce__() -> tuple: ...
    def dst() -> object: ...
    def isoformat() -> str: ...
    def replace(*args, **kwargs) -> object: ...
    def strftime(format) -> object: ...
    def tzname() -> object: ...
    def utcoffset() -> object: ...

class timedelta(object):
    def __reduce__() -> tuple: ...
    def total_seconds() -> int: ...

class tzinfo(object):
    def __reduce__() -> tuple: ...
    def dst(*args, **kwargs) -> object: ...
    def fromutc(*args, **kwargs) -> object:
        raise TypeError()
        raise ValueError()
    def tzname(*args, **kwargs) -> object: ...
    def utcoffset(*args, **kwargs) -> object: ...

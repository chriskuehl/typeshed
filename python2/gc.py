"""Stub file for the 'gc' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, Undefined, GenericType

def collect(*args, **kwargs) -> int:
    raise ValueError()

def disable() -> None: ...

def enable() -> None: ...

def get_count() -> tuple: ...

def get_debug() -> int: ...

def get_objects() -> list: ...

def get_referents(*args, **kwargs) -> list: ...

def get_referrers(*args, **kwargs) -> list: ...

def get_threshold() -> tuple: ...

def is_tracked(*args, **kwargs) -> bool: ...

def isenabled() -> bool: ...

def set_debug(a: int) -> None: ...

def set_threshold(a: int, *args, **kwargs) -> None: ...

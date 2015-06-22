"""Stub file for the 'cStringIO' module."""
# This is an autogenerated file. It serves as a starting point
# for a more precise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

from typing import List, Tuple, Dict, Undefined, GenericType

InputType = Undefined(StringI)
OutputType = Undefined(StringO)
cStringIO_CAPI = Undefined(object)

def StringIO(*args, **kwargs) -> object: ...


class StringI(object):
    def close() -> None: ...
    def flush() -> None: ...
    def getvalue(*args, **kwargs) -> str: ...
    def isatty() -> bool: ...
    def read(*args, **kwargs) -> str: ...
    def readline(*args, **kwargs) -> str: ...
    def readlines(*args, **kwargs) -> List[str]: ...
    def reset() -> None: ...
    def seek(a: int, *args, **kwargs) -> None: ...
    def tell() -> int: ...
    def truncate(*args, **kwargs) -> None:
        raise IOError()

class StringO(object):
    def close() -> None: ...
    def flush() -> None: ...
    def getvalue(*args, **kwargs) -> str: ...
    def isatty() -> bool: ...
    def read(*args, **kwargs) -> str: ...
    def readline(*args, **kwargs) -> str: ...
    def readlines(*args, **kwargs) -> List[str]: ...
    def reset() -> None: ...
    def seek(a: int, *args, **kwargs) -> None: ...
    def tell() -> int: ...
    def truncate(*args, **kwargs) -> None:
        raise IOError()
    def write(a) -> None: ...
    def writelines(*args, **kwargs) -> None: ...

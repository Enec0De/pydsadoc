#!/usr/bin/env python

from abc import abstractmethod
from functools import total_ordering
from typing import Any, Protocol, TypeVar

T = TypeVar("T", bound=object)


def final_class_and_no_instance(class_: type[T]) -> type[T]:
    # No instance.
    def __new__(cls: type[T]) -> T:
        raise TypeError(f"class {class_.__qualname__} can not be instantiated")

    # No inheritance.
    def __init_subclass__(cls: Any) -> None:
        raise TypeError(f"class {class_.__qualname__} can not be inherited")

    # Set up the function.
    __new__.__qualname__ = f"{class_.__qualname__}.___new__"
    __init_subclass__.__qualname__ = f"{class_.__qualname__}.__init_subclass__"

    # Set up the attributes of the class and return it.
    setattr(class_, "__new__", staticmethod(__new__))
    setattr(class_, "__init_subclass__", classmethod(__init_subclass__))
    return class_


@total_ordering
class BaseNode(Protocol):

    @abstractmethod
    def __eq__(self, other: object, /) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: Any, /) -> bool:
        pass

    @property
    @abstractmethod
    def obj(self, /) -> Any:
        pass


@total_ordering
class ProtocolComparable(Protocol):

    @abstractmethod
    def __eq__(self, other: object, /) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: Any, /) -> bool:
        pass

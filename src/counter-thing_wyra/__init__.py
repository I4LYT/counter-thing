# Copyright (C) Arnay Kumar
# This project is under 
from typing import Any


class Counter(object):
    def __init__(self, count: int = None) -> None:
        if count:
            self.count = count
        else:
            self.count = 0

    def increment(self, count: int = None) -> None:
        """
        Increments the src by one or whatever count is.

        :param count:
        :return:
        """
        try:
            if count:
                self.count += count
            else:
                self.count += 1
        except TypeError:
            raise TypeError("Incorrect type")

    def decrement(self, count: int = None) -> None:
        """
        Decrements the src by one or whatever count is.

        :param count:
        :return:
        """
        if count:
            self.count -= count
        else:
            self.count -= 1

    def __str__(self) -> str:
        return str(self.count)

    def __int__(self) -> int:
        return int(self.count)

    def __sub__(self, other) -> float | Any:
        if type(other) is int:
            return self.count - other
        elif isinstance(other, Counter):
            return self.count - other.count
        else:
            raise TypeError('Can only add integers or Counter objects')

    def __add__(self, other) -> float | Any:
        if type(other) is int:
            return self.count + other
        elif isinstance(other, Counter):
            return self.count + other.count
        else:
            raise TypeError('Can only add integers or Counter objects')

    def __repr__(self) -> str:
        return str(f"Counter({self.count})")

    def __truediv__(self, other) -> float | Any:
        try:
            if type(other) is int:
                return self.count / other
            elif isinstance(other, Counter):
                return self.count / other.count
            else:
                raise TypeError('Can only divide integers or Counter objects')
        except ZeroDivisionError:
            return "It is not possible to divide by zero"

    def __floordiv__(self, other) -> float | Any:
        try:
            if type(other) is int:
                return self.count // other
            elif isinstance(other, Counter):
                return self.count // other.count
            else:
                raise TypeError('Can only floor divide integers or Counter objects')
        except ZeroDivisionError:
            return "It is not possible to floor divide by zero"

    def __mod__(self, other) -> float | Any:
        try:
            if type(other) is int:
                return self.count % other
            elif isinstance(other, Counter):
                return self.count % other.count
            else:
                raise TypeError('Can only Divide integers or Counter objects')
        except ZeroDivisionError:
            return "It is not possible to divide by zero"
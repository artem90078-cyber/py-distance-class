from __future__ import annotations
from functools import total_ordering
from typing import Any


@total_ordering
class Distance:
    def __init__(self, km: float) -> None:
        self.km = float(km)

    def __str__(self) -> str:
        return f"Distance: {self.km:.2f} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def _value(self, other: Any) -> float | None:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return float(other)
        return None

    def __add__(self, other: float | int | Distance) -> Distance | Any:
        other_value = self._value(other)
        if other_value is not None:
            return Distance(self.km + other_value)
        return NotImplemented

    def __radd__(self, other: float | int | Distance) -> Distance | Any:
        return self.__add__(other)

    def __iadd__(self, other: float | int | Distance) -> Distance | Any:
        other_value = self._value(other)
        if other_value is not None:
            self.km += other_value
            return self
        return NotImplemented

    def __mul__(self, other: float | int) -> Distance | Any:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other: float | int) -> Distance | Any:
        return self.__mul__(other)

    def __truediv__(self, other: float | int) -> Distance | Any:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Distance(self.km / other)
        return NotImplemented

    def __eq__(self, other: Any) -> bool:
        other_value = self._value(other)
        if other_value is not None:
            return self.km == other_value
        return NotImplemented

    def __lt__(self, other: Any) -> bool:
        other_value = self._value(other)
        if other_value is not None:
            return self.km < other_value
        return NotImplemented

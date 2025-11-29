class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    # Addition
    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    # Multiplication
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    # Division
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Distance(round(self.km / other, 2))
        return NotImplemented

    # Comparison helpers
    def _value(self, other):
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return float(other)
        return NotImplemented

    def __lt__(self, other):
        target = self._value(other)
        if target is NotImplemented:
            return NotImplemented
        return self.km < target

    def __gt__(self, other):
        target = self._value(other)
        if target is NotImplemented:
            return NotImplemented
        return self.km > target

    def __eq__(self, other):
        target = self._value(other)
        if target is NotImplemented:
            return NotImplemented
        return self.km == target

    def __le__(self, other):
        target = self._value(other)
        if target is NotImplemented:
            return NotImplemented
        return self.km <= target

    def __ge__(self, other):
        target = self._value(other)
        if target is NotImplemented:
            return NotImplemented
        return self.km >= target

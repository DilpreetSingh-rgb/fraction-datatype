from math import gcd


class Fraction:

    def __init__(self, numerator=0, denominator=1):

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")

        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        # Keep negative sign in numerator
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Simplify
        common = gcd(abs(numerator), denominator)

        self.num = numerator // common
        self.den = denominator // common

    # --------------------------------
    # String representation
    # --------------------------------

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    # --------------------------------
    # Addition
    # --------------------------------

    def __add__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            return NotImplemented

        num = self.num * other.den + self.den * other.num
        den = self.den * other.den

        return Fraction(num, den)

    def __radd__(self, other):

        return self + other

    # --------------------------------
    # Subtraction
    # --------------------------------

    def __sub__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            return NotImplemented

        num = self.num * other.den - self.den * other.num
        den = self.den * other.den

        return Fraction(num, den)

    def __rsub__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        return other - self

    # --------------------------------
    # Multiplication
    # --------------------------------

    def __mul__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            return NotImplemented

        num = self.num * other.num
        den = self.den * other.den

        return Fraction(num, den)

    def __rmul__(self, other):
        return self * other

    # --------------------------------
    # Division
    # --------------------------------

    def __truediv__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            return NotImplemented

        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        num = self.num * other.den
        den = self.den * other.num

        return Fraction(num, den)

    def __rtruediv__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        return other / self

    # --------------------------------
    # Equality
    # --------------------------------

    def __eq__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            return False

        return self.num == other.num and self.den == other.den

    def __ne__(self, other):
        return not self == other

    # --------------------------------
    # Comparisons
    # --------------------------------

    def __lt__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            return NotImplemented

        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):

        if isinstance(other, int):
            other = Fraction(other)

        if not isinstance(other, Fraction):
            return NotImplemented

        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self > other or self == other

    # --------------------------------
    # Unary operators
    # --------------------------------

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __pos__(self):
        return Fraction(self.num, self.den)

    def __abs__(self):
        return Fraction(abs(self.num), self.den)

    # --------------------------------
    # Conversions
    # --------------------------------

    def __float__(self):
        return self.num / self.den

    def __int__(self):
        return self.num // self.den

    def __bool__(self):
        return self.num != 0

    # --------------------------------
    # Hashing
    # --------------------------------

    def __hash__(self):
        return hash((self.num, self.den))

    # --------------------------------
    # Extra functionality
    # --------------------------------

    def reciprocal(self):

        if self.num == 0:
            raise ZeroDivisionError("Zero does not have a reciprocal")

        return Fraction(self.den, self.num)

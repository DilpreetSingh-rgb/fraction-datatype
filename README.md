# <mark>Fraction Datatype for Python

A reusable `Fraction` datatype built from scratch in Python.

The `fraction.py` module can be downloaded and directly imported into any Python project to create and work with mathematical fractions.

## Features

* Automatic fraction simplification using GCD
* Addition, subtraction, multiplication, and division
* Operations with integers
* Reverse arithmetic operations
* Comparison operators
* Unary operations
* Integer and floating-point conversion
* Boolean evaluation
* Hashable Fraction objects
* Reciprocal calculation
* Zero-division handling
* Denominator validation
* Custom `str()` and `repr()` representations
* Operator overloading

## Installation

No external dependencies are required.

Simply download `fraction.py` and place it in your Python project.

```text
your_project/
│
├── fraction.py
└── main.py
```

Then import the `Fraction` class:

```python
from fraction import Fraction
```

## Basic Usage

```python
from fraction import Fraction

a = Fraction(2, 3)
b = Fraction(4, 6)

print(a)
print(b)
```

Output:

```text
2/3
2/3
```

Fractions are automatically simplified during creation.

```python
f = Fraction(20, 30)

print(f)
```

Output:

```text
2/3
```

## Arithmetic Operations

### Addition

```python
a = Fraction(2, 3)
b = Fraction(1, 6)

print(a + b)
```

Output:

```text
5/6
```

### Subtraction

```python
print(a - b)
```

Output:

```text
1/2
```

### Multiplication

```python
print(a * b)
```

Output:

```text
1/9
```

### Division

```python
print(a / b)
```

Output:

```text
4/1
```

## Operations with Integers

The datatype also supports operations between fractions and integers.

```python
f = Fraction(2, 3)

print(f + 2)
print(2 + f)

print(f - 2)
print(2 - f)

print(f * 3)
print(3 * f)

print(f / 2)
print(2 / f)
```

## Comparisons

Fraction objects can be compared directly:

```python
a = Fraction(2, 3)
b = Fraction(4, 6)

print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
```

Output:

```text
True
False
False
True
False
True
```

## Negative Fractions

Negative denominators are automatically normalized.

```python
print(Fraction(2, -3))
print(Fraction(-2, -3))
```

Output:

```text
-2/3
2/3
```

## Type Conversion

### Float

```python
f = Fraction(2, 3)

print(float(f))
```

Output:

```text
0.6666666666666666
```

### Integer

```python
f = Fraction(7, 3)

print(int(f))
```

Output:

```text
2
```

### Boolean

```python
print(bool(Fraction(2, 3)))
print(bool(Fraction(0, 5)))
```

Output:

```text
True
False
```

## Unary Operations

```python
f = Fraction(2, 3)

print(-f)
print(+f)
print(abs(-f))
```

Output:

```text
-2/3
2/3
2/3
```

## Reciprocal

The reciprocal of a fraction can be obtained using `reciprocal()`.

```python
f = Fraction(2, 3)

print(f.reciprocal())
```

Output:

```text
3/2
```
## Error Handling

The datatype validates invalid operations.

### Zero denominator

```python
f = Fraction(5, 0)
```

Raises:

```text
ZeroDivisionError: Denominator cannot be zero
```

### Division by zero

```python
a = Fraction(2, 3)
b = Fraction(0, 1)

print(a / b)
```

Raises:

```text
ZeroDivisionError: Cannot divide by zero
```

## Operator Overloading

The implementation uses Python's special methods to make `Fraction` objects behave like numeric types.

| Operation  | Special Method  |
| ---------- | --------------- |
| `+`        | `__add__()`     |
| `-`        | `__sub__()`     |
| `*`        | `__mul__()`     |
| `/`        | `__truediv__()` |
| `==`       | `__eq__()`      |
| `<`        | `__lt__()`      |
| `>`        | `__gt__()`      |
| `<=`       | `__le__()`      |
| `>=`       | `__ge__()`      |
| `-f`       | `__neg__()`     |
| `abs(f)`   | `__abs__()`     |
| `float(f)` | `__float__()`   |
| `int(f)`   | `__int__()`     |
| `bool(f)`  | `__bool__()`    |
| `print(f)` | `__str__()`     |

## Project Structure

```text
fraction-datatype/
│
├── fraction.py
├── use.py
├── test_fraction.py
├── README.md
└── LICENSE
```

## Example

A complete example:

```python
from fraction import Fraction

a = Fraction(2, 3)
b = Fraction(4, 6)

print("a =", a)
print("b =", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Equal:", a == b)
print("Float:", float(a))
print("Reciprocal:", a.reciprocal())
```

Output:

```text
a = 2/3
b = 2/3

Addition: 4/3
Subtraction: 0/1
Multiplication: 4/9
Division: 1/1

Equal: True
Float: 0.6666666666666666
Reciprocal: 3/2
```

## Purpose

This project was built to create a reusable Fraction datatype while exploring:

* Object-Oriented Programming
* Operator overloading
* Python's data model
* Mathematical fraction operations
* Input validation
* Code reusability and modular design

## License

This project is open source and available under the MIT License.

from fraction import Fraction


# -------------------------------
# Creating Fractions
# -------------------------------

f1 = Fraction(2, 3)
f2 = Fraction(4, 6)
f3 = Fraction(5, 2)

print("Fractions:")
print("f1 =", f1)
print("f2 =", f2)
print("f3 =", f3)


# -------------------------------
# Automatic Simplification
# -------------------------------

print("\nSimplification:")

f4 = Fraction(20, 30)

print("Fraction(20, 30) =", f4)


# -------------------------------
# Arithmetic Operations
# -------------------------------

print("\nArithmetic Operations:")

print("f1 + f3 =", f1 + f3)
print("f1 - f3 =", f1 - f3)
print("f1 * f3 =", f1 * f3)
print("f1 / f3 =", f1 / f3)


# -------------------------------
# Operations with Integers
# -------------------------------

print("\nOperations with Integers:")

print("f1 + 2 =", f1 + 2)
print("2 + f1 =", 2 + f1)

print("f1 - 2 =", f1 - 2)
print("2 - f1 =", 2 - f1)

print("f1 * 3 =", f1 * 3)
print("3 * f1 =", 3 * f1)

print("f1 / 2 =", f1 / 2)
print("2 / f1 =", 2 / f1)


# -------------------------------
# Comparison Operations
# -------------------------------

print("\nComparisons:")

print("f1 == f2:", f1 == f2)
print("f1 != f2:", f1 != f2)

print("f1 < f3 :", f1 < f3)
print("f1 <= f3:", f1 <= f3)

print("f1 > f3 :", f1 > f3)
print("f1 >= f3:", f1 >= f3)


# -------------------------------
# Unary Operations
# -------------------------------

print("\nUnary Operations:")

print("-f1 =", -f1)
print("+f1 =", +f1)
print("abs(-f1) =", abs(-f1))


# -------------------------------
# Conversions
# -------------------------------

print("\nConversions:")

print("float(f1) =", float(f1))
print("int(f3) =", int(f3))
print("bool(f1) =", bool(f1))


# -------------------------------
# Reciprocal
# -------------------------------

print("\nReciprocal:")

print("f1 =", f1)
print("Reciprocal =", f1.reciprocal())


# -------------------------------
# Hashing / Set
# -------------------------------

print("\nSet:")

a = Fraction(2, 3)
b = Fraction(4, 6)

my_set = {a, b}

print("a =", a)
print("b =", b)
print("Set =", my_set)
print("Number of elements =", len(my_set))


# -------------------------------
# repr()
# -------------------------------

print("\nRepresentation:")

print("str(f1)  =", str(f1))
print("repr(f1) =", repr(f1))
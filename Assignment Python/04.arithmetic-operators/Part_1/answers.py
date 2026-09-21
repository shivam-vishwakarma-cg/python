"""Part 1 - Theory answers for Python arithmetic operators."""

# 1. Arithmetic operators
# Arithmetic operators calculate values. Python uses + addition, - subtraction,
# * multiplication, / true division, // floor division, % modulus, and ** power.

# 2. Division
# / returns true division and normally produces a float. // returns the floor
# of the quotient, which is the greatest integer less than or equal to it.

# 3. Floor division
# -10 / 3 is about -3.333. Flooring moves toward negative infinity, so
# -10 // 3 is -4, not -3.
print("-10 // 3 =", -10 // 3)

# 4. Modulus
# % returns the remainder after floor division. Python keeps the remainder's
# sign consistent with the divisor: -10 % 3 is 2 because -10 = (-4 * 3) + 2.
print("-10 % 3 =", -10 % 3)

# 5. Subtraction of negative numbers
# Subtracting a negative is equivalent to adding its positive opposite.
print("10 - (-5) =", 10 - (-5))

# 6. Operator precedence
# Precedence is the priority Python uses when deciding which operation runs
# first. Multiplication has higher precedence than addition.
print("10 + 5 * 2 =", 10 + 5 * 2)

# 7. Parentheses
# Parentheses have the highest priority and force the enclosed operation first.
print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)

# 8. Exponentiation
# ** is exponentiation. Unary minus is applied after exponentiation unless the
# base is parenthesized, so -2 ** 2 means -(2 ** 2).
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

# 9. Boolean arithmetic
# bool is a subclass of int: True behaves as 1 and False behaves as 0.
print("True + True =", True + True)
print("False * 10 =", False * 10)

# 10. None
# None represents the absence of a value. It is not a number, so arithmetic
# such as None + 1 raises TypeError.
try:
    print(None + 1)
except TypeError as error:
    print("None + 1 ->", type(error).__name__)

# 11. String operations
# + concatenates strings and * repeats a string by an integer.
print("Hello" + "World")
print("Hello" * 3)

# 12. Division by zero
# Division by zero raises ZeroDivisionError.
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("10 / 0 ->", type(error).__name__)

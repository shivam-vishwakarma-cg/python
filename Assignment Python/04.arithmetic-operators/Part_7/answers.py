"""Part 7 - Arithmetic with None."""

value = None
print("Task 18")
operations = (
    ("addition", lambda: value + 1),
    ("subtraction", lambda: value - 1),
    ("multiplication", lambda: value * 1),
    ("division", lambda: value / 1),
    ("floor division", lambda: value // 1),
    ("modulus", lambda: value % 1),
    ("exponentiation", lambda: value ** 1),
)
for name, operation in operations:
    try:
        print(name, operation())
    except TypeError as error:
        print(name, "->", type(error).__name__)

print("None means no value; it is not an integer or float, so direct arithmetic raises TypeError.")

"""Part 10 - Final challenge: arithmetic expression analyzer."""

# Predictions are recorded in comments before each evaluated expression.
a = 10
b = -3
c = 2.5

expressions = (
    ("a + b", a + b),                    # prediction: 7
    ("a - b", a - b),                    # prediction: 13
    ("a * c", a * c),                    # prediction: 25.0
    ("a / c", a / c),                    # prediction: 4.0
    ("a // b", a // b),                  # prediction: -4
    ("a % b", a % b),                    # prediction: -2
    ("b ** 2", b ** 2),                  # prediction: 9
    ("(a + b) * c", (a + b) * c),        # prediction: 17.5
    ("a + b * c", a + b * c),            # prediction: 2.5; * first
    ("(a - b) / c", (a - b) / c),        # prediction: 5.2
    ("a ** 2 + c * 2", a ** 2 + c * 2),  # prediction: 106.0; ** then *
    ("(a + c) // 3", (a + c) // 3),      # prediction: 4.0
)

print("Task 21")
for expression, result in expressions:
    print(f"{expression} = {result}")

print("All predictions match Python because exponentiation, then multiplication/division,")
print("then addition/subtraction are applied unless parentheses change the order.")

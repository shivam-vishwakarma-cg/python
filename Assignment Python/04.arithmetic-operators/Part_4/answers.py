"""Part 4 - Operator precedence and parentheses."""

# Task 11 - Expected results are shown before execution in comments.
# 10 + 5 * 2 -> 20; multiplication first
# 20 - 4 / 2 -> 18.0; division first
# 10 + 20 / 5 * 2 -> 18.0; division and multiplication left to right
# 2 + 3 * 4 ** 2 -> 50; exponentiation, then multiplication
# 100 - 20 // 5 -> 96; floor division first
print("Task 11")
for expression, result in (
    ("10 + 5 * 2", 10 + 5 * 2),
    ("20 - 4 / 2", 20 - 4 / 2),
    ("10 + 20 / 5 * 2", 10 + 20 / 5 * 2),
    ("2 + 3 * 4 ** 2", 2 + 3 * 4 ** 2),
    ("100 - 20 // 5", 100 - 20 // 5),
):
    print(expression, "=", result)

# Task 12 - Parentheses override the normal precedence order.
print("\nTask 12")
comparisons = (
    ("10 + 5 * 2", 10 + 5 * 2),
    ("(10 + 5) * 2", (10 + 5) * 2),
    ("20 - 10 / 2", 20 - 10 / 2),
    ("(20 - 10) / 2", (20 - 10) / 2),
    ("2 + 3 * 4", 2 + 3 * 4),
    ("(2 + 3) * 4", (2 + 3) * 4),
)
for expression, result in comparisons:
    print(expression, "=", result)

"""Part 5 - Boolean arithmetic."""

# bool values act like integers: True is 1 and False is 0.
print("Task 13")
boolean_operations = (
    ("True + False", True + False),
    ("True - False", True - False),
    ("True * False", True * False),
    ("True / 2", True / 2),
    ("True // 2", True // 2),
    ("True % 2", True % 2),
    ("True ** 2", True ** 2),
)
for expression, result in boolean_operations:
    print(f"{expression} = {result!r}, type = {type(result).__name__}")

print("\nTask 14")
for expression, result in (
    ("True + 5", True + 5),
    ("False + 5", False + 5),
    ("True * 10", True * 10),
    ("False * 10", False * 10),
    ("True - 5", True - 5),
    ("False - 5", False - 5),
):
    print(expression, "=", result)

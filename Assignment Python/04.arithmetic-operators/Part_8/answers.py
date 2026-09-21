"""Part 8 - Error handling practice."""

print("Task 19")
examples = (
    ("division by zero", lambda: 10 / 0),
    ("invalid string subtraction", lambda: "Hello" - "World"),
    ("arithmetic with None", lambda: None + 1),
)
for name, operation in examples:
    try:
        print(name, operation())
    except (TypeError, ZeroDivisionError) as error:
        print(name, "->", type(error).__name__, ":", error)

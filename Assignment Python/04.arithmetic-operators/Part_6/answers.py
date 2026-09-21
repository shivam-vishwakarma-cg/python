"""Part 6 - String operations."""

# Task 15 - Concatenation
first_name = "Ada"
last_name = "Lovelace"
print("Task 15")
print("Complete name:", first_name + " " + last_name)

# Task 16 - Repetition; multiplying by a float raises TypeError.
word = "Python"
print("\nTask 16")
print("Repeated word:", word * 3)
try:
    print(word * 2.5)
except TypeError as error:
    print("String * float ->", type(error).__name__)

# Task 17 - Supported and unsupported operations.
print("\nTask 17")
print("string + string ->", "Hello" + "World")
print("string * integer ->", "Hi" * 3)
for label, operation in (
    ("string - string", lambda: "Hello" - "World"),
    ("string / string", lambda: "Hello" / "World"),
):
    try:
        operation()
    except TypeError as error:
        print(label, "->", type(error).__name__)

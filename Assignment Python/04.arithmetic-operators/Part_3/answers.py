"""Part 3 - Practical arithmetic tasks 1 through 10."""

# Task 1 - Basic arithmetic
first_number = 10
second_number = 3
print("Task 1")
print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Floor division:", first_number // second_number)
print("Modulus:", first_number % second_number)
print("Exponentiation:", first_number ** second_number)

# Task 2 - Integer and float
integer_value = 19
float_value = 2.5
print("\nTask 2")
for operation_name, result in (
    ("Addition", integer_value + float_value),
    ("Subtraction", integer_value - float_value),
    ("Multiplication", integer_value * float_value),
    ("Division", integer_value / float_value),
    ("Floor division", integer_value // float_value),
    ("Modulus", integer_value % float_value),
    ("Exponentiation", integer_value ** float_value),
):
    print(f"{operation_name}: {result} ({type(result).__name__})")

# Task 3 - Student marks
maths_mark = 90
science_mark = 85
english_mark = 80
total_marks = maths_mark + science_mark + english_mark
average_marks = total_marks / 3
print("\nTask 3")
print("Total marks:", total_marks)
print("Average marks:", average_marks)

# Task 4 - Product calculation
product_price = 12.50
quantity = 4
print("\nTask 4")
print("Total price:", product_price * quantity)

# Task 5 - Even or odd
number = 19
print("\nTask 5")
print("Even" if number % 2 == 0 else "Odd")

# Task 6 - Division and floor division
positive_left = 10
positive_right = 3
negative_left = -10
negative_right = 3
print("\nTask 6")
print("Positive normal division:", positive_left / positive_right)
print("Positive floor division:", positive_left // positive_right)
print("Negative normal division:", negative_left / negative_right)
print("Negative floor division:", negative_left // negative_right)

# Task 7 - Negative number operations
negative_first = -10
negative_second = -3
print("\nTask 7")
print("Addition:", negative_first + negative_second)
print("Subtraction:", negative_first - negative_second)
print("Multiplication:", negative_first * negative_second)
print("Division:", negative_first / negative_second)
print("Floor division:", negative_first // negative_second)
print("Modulus:", negative_first % negative_second)

# Task 8 - Subtraction edge cases
print("\nTask 8")
print("positive - positive =", 10 - 5)
print("positive - negative =", 10 - (-5))
print("negative - positive =", -10 - 5)
print("negative - negative =", -10 - (-5))

# Task 9 - Floor division edge cases
print("\nTask 9")
for expression, result in (
    ("10 // 3", 10 // 3),
    ("-10 // 3", -10 // 3),
    ("10 // -3", 10 // -3),
    ("-10 // -3", -10 // -3),
):
    print(expression, "=", result)
print("Floor division goes toward negative infinity, rather than merely cutting off decimals.")

# Task 10 - Modulus edge cases
print("\nTask 10")
for expression, result in (
    ("10 % 3", 10 % 3),
    ("-10 % 3", -10 % 3),
    ("10 % -3", 10 % -3),
    ("-10 % -3", -10 % -3),
):
    print(expression, "=", result)
print("The remainder has the same sign as the divisor, or is zero.")

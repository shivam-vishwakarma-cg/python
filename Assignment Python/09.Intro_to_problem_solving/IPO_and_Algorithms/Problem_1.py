# Problem 1: Sum of Two Numbers
# 1. IPO Model
# Input: Two numbers (a, b)
# Process: Calculate a+b
# Output: Sum

# 2. Algorithm
# Start
# Read first number a
# Read second number b
# Calculate sum=a+b
# Print sum
# Stop

# 3. Dry Run
# Test Case 1: Inputs: a=10, b=15
# Process: sum=10+15=25
# Output: 25
# Test Case 2: Inputs: a=−5, b=8
# Process: sum=−5+8=3
# Output: 3

# 4. Python Code
# Python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

total_sum = num1 + num2

print("Sum:", total_sum)
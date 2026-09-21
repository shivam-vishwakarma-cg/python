# Problem 2: Even or Odd
# 1. IPO Model
# Input: A number (n)
# Process: Check if n(mod2)==0
# Output: "Even" or "Odd"

# 2. Algorithm
# Start
# Read number n
# If n%2==0, then:
# Print "Even"
# Else:
# Print "Odd"
# Stop

# 3. Dry Run
# Test Case 1: Input: n=14
# Process: 14%2==0 (True)
# Output: Even
# Test Case 2: Input: n=7
# Process: 7%2==0 (False)
# Output: Odd

# 4. Python Code
# Python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
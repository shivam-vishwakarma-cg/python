# Problem 3: Largest of Three Numbers
# 1. IPO Model
# Input: Three numbers (a, b, c)
# Process: Compare a, b, and c to find the maximum
# Output: Largest number

# 2. Algorithm
# Start
# Read three numbers a, b, c
# If a≥b and a≥c, then:
# largest=a
# Else if b≥a and b≥c, then:
# largest=b
# Else:
# largest=c
# Print largest
# Stop

# 3. Dry Run
# Test Case 1: Inputs: a=12, b=45, c=30
# Process: 12≥45 (False) →45≥12 and 45≥30 (True) →largest=45
# Output: Largest: 45
# Test Case 2: Inputs: a=99, b=10, c=50
# Process: 99≥10 and 99≥50 (True) →largest=99
# Output: Largest: 99

# 4. Python Code
# Python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)
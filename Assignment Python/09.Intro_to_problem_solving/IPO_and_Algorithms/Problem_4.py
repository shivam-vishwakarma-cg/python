# Problem 4: Voting Eligibility
# 1. IPO Model
# Input: Age (age)
# Process: Check if age≥18
# Output: "Eligible to vote" or "Not eligible to vote"

# 2. Algorithm
# Start
# Read age
# If age≥18, then:
# Print "Eligible to vote"
# Else:
# Print "Not eligible to vote"
# Stop

# 3. Dry Run
# Test Case 1: Input: age=20
# Process: 20≥18 (True)
# Output: Eligible to vote
# Test Case 2: Input: age=15
# Process: 15≥18 (False)
# Output: Not eligible to vote

# 4. Python Code
# Python
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
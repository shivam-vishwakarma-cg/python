# Problem 6: Subject Marks Pass/Fail Result
# 1. IPO Model
# Input: Marks of three subjects (m1, m2, m3)
# Process: avg=(m1+m2+m3)/3. Check if avg≥40
# Output: "Pass" or "Fail"

# 2. Algorithm
# Start
# Read three marks m1, m2, m3
# Calculate avg=(m1+m2+m3)/3
# If avg≥40, then:
# Print "Pass"
# Else:
# Print "Fail"
# Stop

# 3. Dry Run
# Test Case 1: Inputs: m1=45, m2=50, m3=55
# Process: avg=(45+50+55)/3=150/3=50.0→50.0≥40 (True)
# Output: Pass
# Test Case 2: Inputs: m1=30, m2=35, m3=40
# Process: avg=(30+35+40)/3=105/3=35.0→35.0≥40 (False)
# Output: Fail

# 4. Python Code
# Python
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

average = (m1 + m2 + m3) / 3

if average >= 40:
    print("Pass")
else:
    print("Fail")
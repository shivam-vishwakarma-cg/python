# Problem 5: Price Discount Calculation
# 1. IPO Model
# Input: Original Price (price)
# Process: If price≥2000, discount=0.20×price, final_price=price−discount. Otherwise, final_price=price
# Output: Final Price

# 2. Algorithm
# Start
# Read price
# If price≥2000, then:
# discount=price×0.20
# final_price=price−discount
# Else:
# final_price=price
# Print final_price
# Stop

# 3. Dry Run
# Test Case 1: Input: price=2500
# Process: 2500≥2000 (True) →discount=2500×0.20=500→final_price=2500−500=2000.0
# Output: Final Price: 2000.0
# Test Case 2: Input: price=1500
# Process: 1500≥2000 (False) →final_price=1500
# Output: Final Price: 1500.0

# 4. Python Code
# Python
price = float(input("Enter item price: "))

if price >= 2000:
    discount = price * 0.20
    final_price = price - discount
else:
    final_price = price

print("Final price:", final_price)
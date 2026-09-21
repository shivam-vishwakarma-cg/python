#task-11

#Python follows operator precedence:

#** — exponentiation
#*, /, //, % — multiplication, division, floor division, modulo
#+, - — addition and subtraction

print(10 + 5 * 2)
print(20 - 4 / 2)
print(10 + 20 / 5 * 2)
print(2 + 3 * 4 ** 2)
print(100 - 20 // 5)

#task-12
# Example 1
print(10 + 5 * 2)       # 20
print((10 + 5) * 2)     # 30

# Example 2
print(20 - 10 / 2)      # 15.0
print((20 - 10) / 2)    # 5.0

# Example 3
print(2 + 3 * 4)        # 14
print((2 + 3) * 4)      # 20

#task-13

c=True
d=False

print("Addition : ",c+d,type(c+d))
print("sub : ",c-d,type(c-d))
print("mul : ",c*d,type(c*d))
print("div : ",c/d,type(c/d))
print("Floor Division :", c // d, type(c // d))
print("Modulus :", c % d, type(c % d))
print("Power :", c ** d, type(c ** d))

#task-14
print(True + 5)
print(False + 5)
print(True * 10)
print(False * 10)
print(True - 5)
print(False - 5)

#task-15

name="Bhavya"
surname="Patel"

print(name+" "+surname)
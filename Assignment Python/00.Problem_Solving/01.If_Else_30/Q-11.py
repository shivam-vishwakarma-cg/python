# year=int(input("enter any year you like"))
# if year%400 == 0:
#     print("it's a leap year buddy")
# else:
#     print("not a leap year")
#don't work in 2024


year=int(input("enter any year you like"))
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("it's a leap year buddy")
else:
    print("not a leap year")

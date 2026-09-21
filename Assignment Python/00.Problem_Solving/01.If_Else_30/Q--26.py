day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if year < 1 or month < 1 or month > 12:
    print("Invalid date")
else:
    if month == 2:
        max_days = 29 if leap_year else 28
    elif month in (4, 6, 9, 11):
        max_days = 30
    else:
        max_days = 31

    if 1 <= day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")
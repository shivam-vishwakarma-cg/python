age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

if 18 <= age <= 25 and marks >= 85 and income <= 300000 and attendance >= 75:
    print("Scholarship Approved")

else:
    print("Scholarship Rejected")

    if age < 18 or age > 25:
        print("Reason: Age must be between 18 and 25")

    if marks < 85:
        print("Reason: Marks below 85")

    if income > 300000:
        print("Reason: Family income exceeds ₹300000")

    if attendance < 75:
        print("Reason: Attendance below 75%")
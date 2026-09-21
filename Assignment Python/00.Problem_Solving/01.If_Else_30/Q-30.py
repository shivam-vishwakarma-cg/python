student_age=int(input("Enter age : "))
marks=float(input("Enter marks : "))
family_income=float(input("enter income : "))
attendence_per=float(input("enter attendece percentage : "))

if student_age>=18 and student_age<=25:
    if marks>=85:
        if attendence_per>=75:
                if family_income<=300000:
                    print("Scholarship Approved")
                else:
                    print("family income greater then 3LPA")
        else:
             print("attendence is less then 75 ")    
    else:
         print("Marks are below 85")
else:
     print("invalid age")
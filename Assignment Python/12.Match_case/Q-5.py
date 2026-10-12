choose=int(input("""1 → View Profile
2 → View Courses
3 → View Marks
4 → View Attendance
5 → Logout"""))
match choose:
    case 1:
        print("Opening View Profile")
    case 2:
        print("Opening View Courses")
    case 3:
        print("Opening View Marks")
    case 4:
        print("Opening View Attendance")
    case _:
        print("Logout")
        
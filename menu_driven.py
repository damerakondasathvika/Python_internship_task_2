from register import *
from enroll import *
from track import *
from certificate import *
print("===== ONLINE COURSE MANAGEMENT SYSTEM =====")
register_student()
display_students()
print("\nPlease Login")
if login_student():
    while True:
        print("\n===== STUDENT DASHBOARD =====")
        print("1. Enroll Course")
        print("2. View Enrollments")
        print("3. Track Progress")
        print("4. View Progress")
        print("5. Generate Certificate")
        print("6. Logout")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            enroll_course()
        elif choice == 2:
            display_enrollments()
        elif choice == 3:
            track_progress()
        elif choice == 4:
            display_progress()
        elif choice == 5:
            generate_certificate()
        elif choice == 6:
            print("Logged Out Successfully!")
            break
        else:
            print("Invalid Choice!")
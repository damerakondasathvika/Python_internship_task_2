from register import *
from enroll import *
from track import *
def generate_certificate():
    student_id = input("Enter Student ID: ")
    if student_id in progress:
        if progress[student_id] == 100:
            print("\n")
            print("====================================")
            print("      COURSE COMPLETION CERTIFICATE")
            print("====================================")
            print("Student Name :", students[student_id]["name"])
            print("Student ID   :", student_id)
            print("Course       :", enrollments[student_id])
            print("Status       : Completed")
            print("====================================")
            print("Congratulations!")
            print("====================================")
        else:
            print("Course not completed yet!")
    else:
        print("Progress record not found!")
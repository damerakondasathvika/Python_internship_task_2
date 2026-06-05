from enroll import *
progress = {}
def track_progress():
    student_id = input("Enter Student ID: ")
    if student_id in enrollments:
        course = enrollments[student_id]
        total_modules = courses[course]
        print("Course:", course)
        print("Total Modules:", total_modules)
        completed_modules = int(input("Enter Completed Modules: "))
        if completed_modules > total_modules:
            print("Invalid Number of Modules!")
        else:
            progress_percentage = int((completed_modules / total_modules) * 100)
            progress[student_id] = progress_percentage
            print("Progress Updated Successfully!")
    else:
        print("Student not enrolled!")
def display_progress():
    print("________________________________________________________")
    print("student_id\tcourse\t\tprogress")
    print("________________________________________________________")
    for student_id, percentage in progress.items():
        print(student_id,"\t",enrollments[student_id],"\t",str(percentage) + "%")
    print()
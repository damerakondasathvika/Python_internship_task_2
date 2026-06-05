from register import *
courses = {
    "Python": 5,
    "Django": 4,
    "Data Science": 6,
    "Web Development": 5
}
enrollments = {}
def enroll_course():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("\nAvailable Courses")
        for course in courses:
            print(course)
        course_name = input("Enter Course Name: ")
        if course_name in courses:
            enrollments[student_id] = course_name
            print("Course Enrolled Successfully!")
        else:
            print("Course Not Available!")
    else:
        print("Student not registered!")
def display_enrollments():
    print("_______________________________________")
    print("student_id\tcourse")
    print("_______________________________________")

    for student_id, course in enrollments.items():
        print(student_id, "\t", course)

    print()
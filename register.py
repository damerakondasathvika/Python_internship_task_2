students = {}
def register_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student already registered!")
    else:
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        students[student_id] = {
            "name": name,
            "email": email,
            "password": password
        }
        print("Registration Successful!")
def display_students():
    print("_______________________________________________________________")
    print("student_id\tname\t\temail")
    print("_______________________________________________________________")
    for student_id, details in students.items():
        print(student_id, "\t", details["name"], "\t", details["email"])
    print("\n")
def login_student():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    for details in students.values():
        if details["email"] == email and details["password"] == password:
            print("Login Successful!")
            return True
    print("Invalid Email or Password!")
    return False

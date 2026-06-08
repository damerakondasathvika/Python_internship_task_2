students = {}
def register_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student already registered!")
        return False
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")
    if password != confirm_password:
        print("Passwords do not match!")
        return False
    students[student_id] = {
        "name": name,
        "email": email,
        "password": password
    }
    print("Registration Successful!")
    return True
def display_students():
    print("_______________________________________________________________")
    print("student_id\tname\t\temail")
    print("_______________________________________________________________")
    for student_id, details in students.items():
        print(student_id, "\t", details["name"], "\t", details["email"])
    print()
def login_student():
    attempts = 4
    while attempts > 0:
        print("\n===== LOGIN PAGE =====")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        for details in students.values():
            if details["email"] == email and details["password"] == password:
                print("Login Successful!")
                return True
        attempts -= 1
        if attempts > 0:
            print(f"Invalid Email or Password! {attempts} attempt(s) left")
        else:
            print("Account Locked! Login Failed.")
            return False
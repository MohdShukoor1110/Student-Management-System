def add_student(students_details):
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    score = int(input("Enter student score (1-10): "))
    email = input("Enter student email: ")
    
    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Score": score,
        "Email": email
    }
    students_details.append(student)
    print("Student added successfully!\n")

def view_students(students_details):
    if not students_details:
        print("No student details found.\n")
        return
    for student in students_details:
        print(f"ID : {student['ID']}\n"+
              f"Name : {student['Name']}\n"+
              f"Age : {student['Age']}\n"+
              f"Score : {student['Score']}\n"
              f"Email-ID : {student['Email']}")
    print()

def update_student(students_details):
    student_id = int(input("Enter student ID to update: "))
    for student in students_details:
        if student['ID'] == student_id:
            student['Name'] = input("Enter new name: ")
            student['Age'] = int(input("Enter new age: "))
            student['Score'] = int(input("Enter new score (1-10): "))
            student['Email'] = input("Enter new email: ")
            print("Student information updated successfully!\n")
            return
    print("Student ID not found.\n")

def delete_student(students_details):
    student_id = int(input("Enter student ID to delete: "))
    for student in students_details:
        if student['ID'] == student_id:
            students_details.remove(student)
            print("Student details deleted successfully!\n")
            return
    print("Student ID not found.\n")

def display_menu():
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update a student's information")
    print("4. Delete a student")
    print("5. Exit")

def student_management_system():
    students_details = []
    while True:
        display_menu()
        choice = input("---> Enter your choice: ")
        if choice == '1':
            add_student(students_details)
        elif choice == '2':
            view_students(students_details)
        elif choice == '3':
            update_student(students_details)
        elif choice == '4':
            delete_student(students_details)
        elif choice == '5':
            print("Exiting the Program. Thank You")
            break
        else:
            print("Invalid choice. Please enter in 1-5 number.\n")
student_management_system()
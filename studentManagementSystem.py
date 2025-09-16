"""
A list to store all student details as dictionaries
"""
students_details = []

"""
This function prompts the user to enter a new student's details and adds them as a dictionary to the students_details list.
"""
def add_student(students_details):
    print()
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    score = int(input("Enter student score (1-10): "))
    email = input("Enter student email: ")
    
    """
    Create a dictionary to hold the student's information
    """
    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Score": score,
        "Email": email
    }
    students_details.append(student)
    print("Student added successfully!\n")

"""
This function iterates through the students_details list and prints the details of each student in a readable format.
"""
def view_students(students_details):
    print()
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

"""
This function updates an existing student's information by searching for their ID.
"""
def update_student(students_details):
    print()
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

"""
This function removes a student's record from the list based on their ID.
"""
def delete_student(students_details):
    print()
    student_id = int(input("Enter student ID to delete: "))
    for student in students_details:
        if student['ID'] == student_id:
            students_details.remove(student)
            print("Student details deleted successfully!\n")
            return
    print("Student ID not found.\n")

"""
This function simply prints the main menu of the program.
"""
def display_menu():
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update a student's information")
    print("4. Delete a student")
    print("5. Exit")

"""
This is the main function that runs the student management system. It contains the main loop and handles user input.
"""
def student_management_system():
    
    # The main program loop
    while True:
        display_menu()
        choice = input("---> Enter your choice: ")
        
        # Call the appropriate function based on the user's choice
        if choice == '1':
            add_student(students_details)
        elif choice == '2':
            view_students(students_details)
        elif choice == '3':
            update_student(students_details)
        elif choice == '4':
            delete_student(students_details)
        elif choice == '5':
            # Break the loop to exit the program
            print()
            print("Exiting the Program. Thank You")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please enter in 1-5 number.\n")

# Start the program by calling the main function
student_management_system()
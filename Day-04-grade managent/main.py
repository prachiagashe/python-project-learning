student_grades={ }

def add_student(name,grade):
    student_grades[name]=grade
    print(f"Added {name} with a {grade} grade.")

def update_stdent(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updtated {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

def display_student_grades():
    if student_grades:
        print("\n Student Grades: ")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No student found.")

while True:
    print("\n=== Student Grade Management ====")
    print("1. Add Students:")
    print("2. Update Students:")
    print("3. Delete Students:")
    print("4. Display Students:")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":
        name=input("Enter student name: ")
        grade= input("Enter grade: ")
        add_student(name,grade)
    elif choice =="2":
        name=input("Enter student name: ")
        grade= input("Enter grade: ")
        update_stdent(name,grade)

    elif choice =="3":
        name=input("Enter student name: ")
        delete_student(name,grade)

    elif choice =="4":
        display_student_grades()
    elif choice =="5":
        print("Thank You")
        break
    else:
        print("Invalid choice. Please try again.")
        




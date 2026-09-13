student_grades={ }
def add_student(name,grade):
    student_grades[name]=grade
    print(f"Added {name} with a {grade} grade.")

def update_stdents(name,grade):
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
        print(f"{name is not found!}")

def display_



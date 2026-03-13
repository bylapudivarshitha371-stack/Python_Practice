students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    students.append({"Name": name, "Roll": roll, "Marks": marks})
    print("Student Added Successfully!")

def view_students():
    for s in students:
        print(s)

def search_student():
    roll = input("Enter roll number: ")
    for s in students:
        if s["Roll"] == roll:
            print("Student Found:", s)
            return
    print("Student not found")

while True:
    print("\n1.Add Student\n2.View Students\n3.Search Student\n4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    else:
        break

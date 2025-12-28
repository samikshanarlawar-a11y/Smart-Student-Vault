import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def create_student():
    students = load_data()
    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            print("ID already exists!\n")
            return

    student = {
        "id": sid,
        "name": input("Enter Name: "),
        "branch": input("Enter Branch: "),
        "year": input("Enter Year: ")
    }

    students.append(student)
    save_data(students)
    print("Student saved successfully!\n")

def display_students():
    students = load_data()
    if not students:
        print("No records found.\n")
        return

    print("\n--- Student Records ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Branch: {s['branch']} | Year: {s['year']}")
    print()

def find_student():
    sid = input("Enter Student ID to search: ")
    students = load_data()

    for s in students:
        if s["id"] == sid:
            print("\nStudent Found:")
            print(s, "\n")
            return
    print("Student not found!\n")

def remove_student():
    sid = input("Enter Student ID to delete: ")
    students = load_data()
    updated = [s for s in students if s["id"] != sid]

    if len(students) == len(updated):
        print("Student ID not found!\n")
    else:
        save_data(updated)
        print("Student deleted successfully!\n")

def menu():
    while True:
        print("====== Smart Student Vault ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            find_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Exiting Vault...")
            break
        else:
            print("Invalid choice!\n")

menu()
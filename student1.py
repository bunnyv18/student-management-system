import json

FILE_NAME = "students.txt"

# Load existing data
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save data to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)

students = load_students()

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("✅ Student added & saved\n")


def view_students():
    if not students:
        print("No students found\n")
        return

    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()


def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found: {s}")
            return
    print("❌ Student not found\n")


def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("🗑 Student deleted & updated\n")
            return
    print("❌ Student not found\n")

def update_student():
    roll = input("Enter roll number to update: ")
    for s in students:
        if s["roll"] == roll:
            new_marks = int(input("Enter new marks: "))
            s["marks"] = new_marks
            save_students(students)
            print("✅ Marks updated\n")
            return
    print("❌ Student not found\n")

def average_marks():
    if not students:
        print("No data\n")
        return

    total = sum(s["marks"] for s in students)
    avg = total / len(students)

    print(f"Average Marks: {avg}\n")


def find_topper():
    if not students:
        print("No data\n")
        return

    topper = max(students, key=lambda x: x["marks"])
    print(f"Topper: {topper['name']} (Marks: {topper['marks']})\n")

def sort_students():
    if not students:
        print("No data\n")
        return

    sorted_list = sorted(students, key=lambda x: x["marks"], reverse=True)

    print("📊 Students sorted by marks:")
    for s in sorted_list:
        print(f"{s['name']} - {s['marks']}")
    print()


while True:
     print("\n===== STUDENT MENU =====")
     print("1. Add Student")
     print("2. View Students")
     print("3. Search Student")
     print("4. Delete Student")
     print("5. Exit")
     print("6. Average Marks")
     print("7. Find Topper")
     print("8. Update Marks")
     print("9. Sort Students")
     print("========================")
     choice = input("Enter choice: ")

     if choice == '1':
        add_student()
     elif choice == '2':
        view_students()
     elif choice == '3':
        search_student()
     elif choice == '4':
        delete_student()
     elif choice == '5':
        print("Exiting...")
     elif choice == '6':
        average_marks()
     elif choice == '7':
        find_topper()
     elif choice == '8':
        update_student()
     elif choice == '9':
        sort_students()
        break
     else:
        print("Invalid choice\n")
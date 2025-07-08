import json
import os

DATA_FILE = 'students_data.json'

# Check if file exists, if not create it
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Load data from file
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Add student
def add_student():
    data = load_data()
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {"roll": roll, "name": name, "marks": marks}
    data.append(student)
    save_data(data)
    print("✅ Student added successfully!")

# View all
def view_students():
    data = load_data()
    print("\n--- Student Records ---")
    for student in data:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Marks: {student['marks']}")

# Search by roll
def search_student():
    roll = input("Enter Roll No to search: ")
    data = load_data()
    for student in data:
        if student['roll'] == roll:
            print(f"✅ Found: {student}")
            return
    print("❌ Student not found.")

# Update student
def update_student():
    roll = input("Enter Roll No to update: ")
    data = load_data()
    for student in data:
        if student['roll'] == roll:
            student['name'] = input("Enter new name: ")
            student['marks'] = input("Enter new marks: ")
            save_data(data)
            print("✅ Student updated!")
            return
    print("❌ Student not found.")

# Delete student
def delete_student():
    roll = input("Enter Roll No to delete: ")
    data = load_data()
    new_data = [student for student in data if student['roll'] != roll]
    save_data(new_data)
    print("✅ Student deleted (if existed).")

# Main menu
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

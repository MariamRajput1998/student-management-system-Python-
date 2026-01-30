from student import Student

student_obj = Student()

def display_students(students):
    if not students:
        print("📭 No records found")
        return

    print("\nID | Name | Age | Course | Email")
    print("-" * 50)
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['age']} | {s['course']} | {s['email']}")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        # ---------- ADD ----------
        if choice == "1":
            student = {
                "name": input("Name: "),
                "age": int(input("Age: ")),
                "course": input("Course: "),
                "email": input("Email: ")
            }
            student_obj.add_student(student)

        # ---------- VIEW ----------
        elif choice == "2":
            students = student_obj.view_students()
            display_students(students)

        # ---------- UPDATE ----------
        elif choice == "3":
            student = {
                "id": int(input("ID: ")),
                "name": input("New Name: "),
                "age": int(input("New Age: ")),
                "course": input("New Course: "),
                "email": input("New Email: ")
            }
            student_obj.update_student(student)

        # ---------- DELETE ----------
        elif choice == "4":
            sid = int(input("Enter ID: "))
            student_obj.delete_student(sid)

        # ---------- SEARCH ----------
        elif choice == "5":
            print("1. Search by ID")
            print("2. Search by Name")
            ch = input("Choice: ")

            if ch == "1":
                sid = int(input("Enter ID: "))
                display_students(student_obj.search_by_id(sid))

            elif ch == "2":
                name = input("Enter Name: ")
                display_students(student_obj.search_by_name(name))

            else:
                print("❌ Invalid search option")

        # ---------- EXIT ----------
        elif choice == "6":
            student_obj.close()
            print("👋 Exiting program")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    menu()

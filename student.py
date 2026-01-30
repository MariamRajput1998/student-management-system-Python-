from db_connection import Database

class Student:
    def __init__(self):
        self.db = Database.get_connection()
        self.cursor = self.db.cursor(dictionary=True)

    def add_student(self, student):
        sql = """
        INSERT INTO students (name, age, course, email)
        VALUES (%(name)s, %(age)s, %(course)s, %(email)s)
        """
        self.cursor.execute(sql, student)
        self.db.commit()
        print("✅ Student added successfully!")

    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def update_student(self, student):
        sql = """
        UPDATE students
        SET name=%(name)s, age=%(age)s, course=%(course)s, email=%(email)s
        WHERE id=%(id)s
        """
        self.cursor.execute(sql, student)
        self.db.commit()
        print("✏️ Student updated successfully!")

    def delete_student(self, student_id):
        self.cursor.execute(
            "DELETE FROM students WHERE id=%s", (student_id,)
        )
        self.db.commit()
        print("🗑️ Student deleted successfully!")

    def search_by_id(self, student_id):
        self.cursor.execute(
            "SELECT * FROM students WHERE id=%s", (student_id,)
        )
        return self.cursor.fetchall()

    def search_by_name(self, name):
        self.cursor.execute(
            "SELECT * FROM students WHERE name LIKE %s",
            ('%' + name + '%',)
        )
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.db.close()

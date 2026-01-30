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


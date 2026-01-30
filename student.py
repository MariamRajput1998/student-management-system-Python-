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

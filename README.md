# student-management-system-Python-
A lightweight command-line interface (CLI) tool for managing student data. Built with a focus on Object-Oriented Programming (OOP) principles and persistent file storage. Add, Update, View, Search, and Delete student records. Persistent data storage using MySQL. Search functionality by Student ID.
Developer: Mariam Safdar & Ayesha Mehtab<br>

<h2>Features:</h2>
#Student Data Management (CRUD operations): The primary function is to manage student records efficiently. This includes:
#Adding new students: Entering details such as name, age, ID, course and email into the MySQL database.
#Viewing student details: Displaying records of all students or a specific student via the command line.
#Updating student information: Modifying existing records (e.g., updating phone numbers, grades, or personal details).
#Deleting student records: Removing student entries from the database, typically using a unique identifier like a student ID or roll number.
#Search and Filter Functionality: Users can search for specific student records using criteria such as ID, name, or roll number to quickly retrieve information.
#Database Connectivity: The system uses a Python library (like mysql-connector-python or pymysql) to establish a connection with the MySQL database, ensuring data integrity and secure storage.
#Command Line Interface (CLI): The system provides a simple, menu-driven command-line interface, allowing users to interact by selecting options. 
Benefits of this Approach
Simplicity: The CLI keeps the application lightweight and focused solely on core logic and database interaction, without needing a complex graphical user interface (GUI).
Portability: The application can run on various operating systems (Windows, macOS, Linux) as long as Python and MySQL are installed.
Efficiency: It is effective for environments where manual record-keeping is replaced by an automated, digital system, reducing manual errors and improving data accessibility. 
Overall, this type of system is a foundational tool for automating administrative tasks in an educational setting. 

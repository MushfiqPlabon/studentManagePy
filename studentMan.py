class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def get_student_by_id(cls, student_id):
        for student in cls.student_list:
            if student.get_student_id() == student_id:
                return student
        return None

class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def is_enrolled(self):
        return self.__is_enrolled

    def enroll_student(self):
        if self.__is_enrolled:
            raise ValueError(f"{self.__name} is already enrolled.")
        self.__is_enrolled = True

    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError(f"{self.__name} is not enrolled.")
        self.__is_enrolled = False

    def view_student_info(self):
        print("Student ID:", self.__student_id)
        print("Name:", self.__name)
        print("Department:", self.__department)
        print("Enrolled:", self.__is_enrolled)

Student("101", "Antor", "CSE")
Student("102", "Tanvir", "EEE")
Student("103", "Rafin", "BBA")
Student("104", "Mamun", "BSS")
Student("105", "Evan", "LLB")
Student("106", "Sizan", "MIS")
Student("108", "Ratul", "IT")
Student("109", "Mridul", "CS")
Student("110", "Ali", "ECE")

while True:
    print("\n--- Student Management System ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(StudentDatabase.student_list) == 0:
            print("No students found.")
        else:
            for student in StudentDatabase.student_list:
                print("\n-----------------")
                student.view_student_info()

    elif choice == "2":
        sid = input("Enter Student ID to enroll: ")
        student = StudentDatabase.get_student_by_id(sid)
        if student:
            try:
                student.enroll_student()
                print(f"{student.get_name()} has been enrolled.")
            except ValueError as e:
                print(e)
        else:
            print("Error: Student ID not found.")

    elif choice == "3":
        sid = input("Enter Student ID to drop: ")
        student = StudentDatabase.get_student_by_id(sid)
        if student:
            try:
                student.drop_student()
                print(f"{student.get_name()} has been dropped.")
            except ValueError as e:
                print(e)
        else:
            print("Error: Student ID not found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
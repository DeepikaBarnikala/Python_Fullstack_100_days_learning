# ==========================================
# UNIVERSITY MANAGEMENT SYSTEM
# ==========================================


# Parent Student Class
class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

        # Encapsulation
        self.__courses = []
        self.__grades = {}

    # Polymorphic method
    def enroll(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

            # Add student to course roster
            course.add_student(self)

            print(self.name, "enrolled in", course.course_name)
        else:
            print(self.name, "is already enrolled in",
                  course.course_name)

    # Polymorphic method
    def view_schedule(self):
        print("\nSchedule of", self.name)

        if len(self.__courses) == 0:
            print("No courses enrolled.")
        else:
            for course in self.__courses:
                print(course.course_name, "-", course.schedule)

    def add_grade(self, course, grade):
        if course in self.__courses:
            self.__grades[course] = grade
        else:
            print("Student is not enrolled in this course.")

    def view_grades(self):
        print("\nGrades of", self.name)

        if len(self.__grades) == 0:
            print("No grades available.")
        else:
            for course, grade in self.__grades.items():
                print(course.course_name, "-", grade)


# ==========================================
# UNDERGRADUATE STUDENT
# ==========================================

class UndergraduateStudent(Student):

    # Polymorphism
    def enroll(self, course):
        print("\nUndergraduate Enrollment")
        super().enroll(course)

    # Polymorphism
    def view_schedule(self):
        print("\nUndergraduate Student Schedule")
        super().view_schedule()


# ==========================================
# GRADUATE STUDENT
# ==========================================

class GraduateStudent(Student):

    # Polymorphism
    def enroll(self, course):
        print("\nGraduate Enrollment")
        super().enroll(course)

    # Polymorphism
    def view_schedule(self):
        print("\nGraduate Student Schedule")
        super().view_schedule()


# ==========================================
# COURSE CLASS
# ==========================================

class Course:

    def __init__(self, course_id, course_name, schedule):
        self.course_id = course_id
        self.course_name = course_name
        self.schedule = schedule

        # Student roster
        self.__students = []

        # Faculty assigned to course
        self.faculty = None

    def add_student(self, student):
        if student not in self.__students:
            self.__students.append(student)

    def assign_faculty(self, faculty):
        self.faculty = faculty

    # Abstraction
    # User only calls this method to see the roster.
    # Internal list implementation is hidden.
    def view_student_roster(self):
        print("\nStudent Roster for", self.course_name)

        if len(self.__students) == 0:
            print("No students enrolled.")
        else:
            for student in self.__students:
                print(student.student_id, "-", student.name)


# ==========================================
# FACULTY CLASS
# ==========================================

class Faculty:

    def __init__(self, faculty_id, name):
        self.faculty_id = faculty_id
        self.name = name

        # Encapsulation
        self.__courses = []

    def assign_course(self, course):

        if course not in self.__courses:
            self.__courses.append(course)

            course.assign_faculty(self)

            print(
                course.course_name,
                "assigned to",
                self.name
            )

    # Faculty can view assigned courses
    def view_course_assignments(self):

        print("\nCourses assigned to", self.name)

        if len(self.__courses) == 0:
            print("No courses assigned.")
        else:
            for course in self.__courses:
                print(
                    course.course_id,
                    "-",
                    course.course_name
                )

    # Faculty can view student rosters
    def view_student_rosters(self):

        print("\nStudent Rosters handled by", self.name)

        if len(self.__courses) == 0:
            print("No courses assigned.")
        else:
            for course in self.__courses:

                print("\nCourse:", course.course_name)

                course.view_student_roster()


# ==========================================
# UNIVERSITY CLASS
# ==========================================

class University:

    def __init__(self, name):

        self.name = name

        # Lists used to manage university data
        self.students = []
        self.courses = []
        self.faculty = []

    # Add student
    def add_student(self, student):
        self.students.append(student)

    # Add course
    def add_course(self, course):
        self.courses.append(course)

    # Add faculty
    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    # Abstraction
    # Administrator doesn't need to know how the
    # student list is internally managed.
    def show_students(self):

        print("\nStudents in", self.name)

        for student in self.students:
            print(
                student.student_id,
                "-",
                student.name
            )

    def show_courses(self):

        print("\nCourses in", self.name)

        for course in self.courses:
            print(
                course.course_id,
                "-",
                course.course_name
            )

    def show_faculty(self):

        print("\nFaculty in", self.name)

        for faculty in self.faculty:
            print(
                faculty.faculty_id,
                "-",
                faculty.name
            )


# ==========================================
# DEPARTMENT CLASS
# Inherits from University
# ==========================================

class Department(University):

    def __init__(self, university_name, department_name):

        # Calling parent constructor
        super().__init__(university_name)

        self.department_name = department_name

    def show_department(self):

        print("\nUniversity:", self.name)
        print("Department:", self.department_name)


# ==========================================
# CREATING OBJECTS
# ==========================================

# University object
university = University("ANITS University")


# Course objects
course1 = Course(
    "C101",
    "Python Programming",
    "Monday 10:00 AM"
)

course2 = Course(
    "C102",
    "Database Management",
    "Wednesday 11:00 AM"
)


# Student objects
student1 = UndergraduateStudent(
    "S101",
    "Deepika"
)

student2 = GraduateStudent(
    "S102",
    "Priya"
)


# Faculty object
faculty1 = Faculty(
    "F101",
    "Dr. Saketh Reddy"
)


# Department object
department1 = Department(
    "ANITS University",
    "EEE"
)


# ==========================================
# ADDING DATA TO UNIVERSITY
# ==========================================

university.add_student(student1)
university.add_student(student2)

university.add_course(course1)
university.add_course(course2)

university.add_faculty(faculty1)


# ==========================================
# FACULTY ASSIGNMENT
# ==========================================

faculty1.assign_course(course1)
faculty1.assign_course(course2)


# ==========================================
# STUDENT ENROLLMENT
# ==========================================

student1.enroll(course1)
student1.enroll(course2)

student2.enroll(course2)


# ==========================================
# VIEW COURSE SCHEDULE
# ==========================================

student1.view_schedule()
student2.view_schedule()


# ==========================================
# ADD AND VIEW GRADES
# ==========================================

student1.add_grade(course1, "A")
student1.add_grade(course2, "B+")

student2.add_grade(course2, "A+")

student1.view_grades()
student2.view_grades()


# ==========================================
# FACULTY COURSE ASSIGNMENTS
# ==========================================

faculty1.view_course_assignments()


# ==========================================
# FACULTY STUDENT ROSTERS
# ==========================================

faculty1.view_student_rosters()


# ==========================================
# UNIVERSITY INFORMATION
# ==========================================

university.show_students()
university.show_courses()
university.show_faculty()


# ==========================================
# DEPARTMENT INFORMATION
# ==========================================

department1.show_department()

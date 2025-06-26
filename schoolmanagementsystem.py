class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print("Name: ",self.name, "ID:" ,self.person_id)

class Student(Person):
    def __init__(self, name, person_id, grade_level):
        super().__init__(name, person_id)
        self.grade_level = grade_level
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(self.name ,"has enrolled in",course.")

    def view_courses(self):
        print(f"{self.name}'s Courses: {', '.join(self.courses)}")

class Teacher(Person):
    def __init__(self, name, person_id, subject):
        super().__init__(name, person_id)
        self.subject = subject
        self.assigned_classes = []

    def assign_class(self, class_name):
        self.assigned_classes.append(class_name)
        print(f"{self.name} has been assigned to {class_name}.")

    def view_classes(self):
        print(f"{self.name} teaches: {', '.join(self.assigned_classes)}")

class Admin(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.managed_users = []

    def add_user(self, person):
        self.managed_users.append(person)
        print(f"Admin {self.name} added {person.name} to the system.")

    def view_users(self):
        print(f"Admin {self.name} manages the following users:")
        for user in self.managed_users:
            print(f"- {user.name} ({type(user).__name__})")
            
# Create instances
student1 = Student("Alice", "S001", "10th Grade")
teacher1 = Teacher("Mr. Smith", "T001", "Mathematics")
admin1 = Admin("Mrs. Johnson", "A001")

# Students enroll in courses
student1.enroll_course("Algebra")
student1.enroll_course("Biology")

# Teacher assigns classes
teacher1.assign_class("10A")
teacher1.assign_class("10B")

# Admin adds users
admin1.add_user(student1)
admin1.add_user(teacher1)

# View info
student1.display_info()
student1.view_courses()

teacher1.display_info()
teacher1.view_classes()

admin1.display_info()
admin1.view_users()

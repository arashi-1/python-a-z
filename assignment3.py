class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User Name: {self.name}, Email: {self.email}"


class Instructor(User):
    def __init__(self, name, email, subject_expertise):
        super().__init__(name, email)
        self.subject_expertise = subject_expertise
        self.content_uploaded = []

    def upload_content(self, content):
        self.content_uploaded.append(content)
        return f"Content '{content}' uploaded."

    def display_info(self):
        return f"Instructor: {self.name}, Email: {self.email}, Expertise: {self.subject_expertise}"


class CourseCreator(Instructor):
    def __init__(self, name, email, subject_expertise):
        super().__init__(name, email, subject_expertise)
        self.courses = {}

    def create_course(self, course_name, modules):
        self.courses[course_name] = modules
        return f"Course '{course_name}' created with modules: {modules}"

    def display_info(self):
        return (f"Course Creator: {self.name}, Email: {self.email}, "
                f"Expertise: {self.subject_expertise}, Courses: {list(self.courses.keys())}")


creator = CourseCreator("Alice", "alice@example.com", "Data Science")
print(creator.display_info())

print(creator.upload_content("Intro to ML Video"))
print(creator.create_course("Machine Learning 101", ["Intro", "Regression", "Classification"]))

print(creator.display_info())
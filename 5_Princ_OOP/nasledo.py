

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_info(self):
        return f"{self.name}, {self.email}"


class Student(User):
    def watch_video(self):
        print("Смотрю")


class Mentor(User):
    def check_homework(self):
        print("Проверяю")


s = Student("Вася", "d@d.ru")
print(s.get_info())
print(s.email)

class CreditMixin:
    price = 0
    long = 0

    def credit(self):
        """Рассрочка"""
        return f"Цена с учетом рассрочки - {self.price/self.long}"


class Course:
    """Курсы"""

    def __init__(self, price: float, name: str, long: int):
        self.price = price
        self.name = name
        self.long = long

    def get_price(self):
        """Цена за курс"""
        return f" Цена за курс составит {self.price}"

    def get_info(self):
        """Получение информации о курсах"""
        return f"Название курса - {self.name}, длительность курса - {self.long}"


class AIcourse(Course, CreditMixin):
    """Курс AI"""
    pass


class CourseProject(Course, CreditMixin):

    def __init__(self, price: float, name: str, long: int, project_name: str):
        super().__init__(price, name, long)
        self.project_name = project_name

    def get_project_name(self):
        return self.project_name


course = CourseProject(1000, "Name", 5, "project")
print(course.credit())
print(course.get_info())
print(course.get_project_name())

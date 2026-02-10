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


class AIcourse(Course):
    """Курс AI"""

    def credit(self):
        """Рассрочка"""
        return f"Цена с учетом рассрочки - {self.price/self.long}"


class CourseProject(Course):

    def __init__(self, price: float, name: str, long: int, project_name: str):
        super().__init__(price, name, long)
        self.project_name = project_name

    def credit(self):
        """Рассрочка"""
        return f"Цена с учетом рассрочки - {self.price/self.long}"

    def get_project_name(self):
        return self.project_name


course = CourseProject(1000, "Name", 5, "project")
print(course.credit())
print(course.get_info())
print(course.get_project_name())

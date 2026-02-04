"""Метод - это функция внутри класса, которая описывает поведение объекта. 
Если атрибут отвечает за данные, то метод за действия"""


class Task:
    """Задача"""
    done: bool = False
    title: str

    def set_info(self, text: str):
        """Установка title"""
        self.title = text

    def get_info(self):
        """Получение данных задачи"""
        return self.title


task = Task()  # Сделать экземпляр
task.set_info("Сделать лекцию")
print(task.get_info())  # Вызов метода

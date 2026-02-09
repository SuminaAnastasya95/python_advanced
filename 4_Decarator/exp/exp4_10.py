class CallCounter:
    def __init__(self):
        # Инициализируем словарь или переменную для хранения функции и её счетчика
        self.count = 0
        self.func = None

    def __call__(self, func):
        # Метод __call__ вызывается один раз при декорировании функции
        self.func = func

        # Возвращаем wrapper, который будет вызываться каждый раз
        def wrapper(*args, **kwargs):
            self.count += 1
            print(f"Call #{self.count}")
            return self.func(*args, **kwargs)

        return wrapper


# Создаем экземпляр декоратора
counter = CallCounter()

# Применяем его к функции


@counter
def say_hello():
    print("Hello!")


@counter
def say_bye():
    print("Bye!")


# Проверка:
say_hello()
say_hello()
say_bye()

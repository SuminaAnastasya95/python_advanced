

from functools import wraps


def limit_calls(max_calls: int):
    def decorator(fn):
        @wraps(fn)
        def wrapper(self, *args, **kwargs):
            count_atrr = f"_{fn.__name__}_count"
            current = getattr(self, count_atrr, 0)
            if current >= max_calls:
                raise RuntimeError("Закончились запуски")
            setattr(self, count_atrr, current+1)
            print(f"[LOG] {fn.__qualname__} called {current + 1}/ {max_calls}")
            return fn(self, *args, **kwargs)
        return wrapper
    return decorator


class Engine:
    """Двигатель"""
    @limit_calls(3)
    def start(self):
        """Запуск"""
        print("Двигатель запущен")


car = Engine()

car.start()
car.start()
car.start()
car.start()  # <---- Ошибка Runtime Error

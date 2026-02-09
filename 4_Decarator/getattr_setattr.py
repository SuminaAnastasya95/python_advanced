

# class User:
#     age: float


# u = User()
# setattr(u, "age", 10)
# print(getattr(u, "age"))

class Command:
    def start(self): print("Strat")
    def stop(self): print("Stop")
    def help(self): print("Help")


cmd = Command()
action = input("Введите команду")

if hasattr(cmd, action):
    getattr(cmd, action)()
else:
    print("Команда не найдена")

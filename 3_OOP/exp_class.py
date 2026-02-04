'''Демо модуль'''


class User:
    '''Пользователь системы'''
    email: str
    name: str
    age: int = 39


print(type(User))  # <class 'type'>

userMaria = User()
print(userMaria)  # <__main__.User object at 0x000001CE7B0F6A50>

userAnton = User()
print(userAnton)  # <__main__.User object at 0x000001F2446B4B90>


userAnton.email = "a@a.ru"
userAnton.name = "Anton"
print(userAnton.email)  # a@a.ru
# Если атрибут не передан AttributeError: 'User' object has no attribute 'age'
print(userAnton.age)

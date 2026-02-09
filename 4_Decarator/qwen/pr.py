# def compose(f, g):
#     # Твой код здесь
#     pass

# # Проверка:
# def add_one(x):
#     return x + 1

# def double(x):
#     return x * 2

# # Создаём функцию: сначала ×2, потом +1
# f = compose(add_one, double)
# print(f(5))  # 11 → (5 * 2 = 10) → (10 + 1 = 11)

# # Создаём функцию: сначала +1, потом ×2
# g = compose(double, add_one)
# print(g(5))  # 12 → (5 + 1 = 6) → (6 * 2 = 12)


def make_counter(start):
    def counter():
        nonlocal start
        start += 1
        return start
    return counter


c1 = make_counter(0)
c2 = make_counter(10)

print(c1())  # ?
print(c1())  # ?
print(c2())  # ?
print(c1())  # ?

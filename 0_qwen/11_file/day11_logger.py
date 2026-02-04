# Напиши функцию log_test(name, status), которая:
# дописывает в файл test_log.txt строку вида:
# [2025-01-07 10:30:00] Тест 'login_test' — passed
# использует текущее время (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# log_test("login_valid", "passed")
# log_test("logout", "failed")

from datetime import datetime

status_list = ["passed", "not_pass",  "failed"]


def log_test(name: str, status: str):
    if status not in status_list:
        print(f"Такого {status} нет в списке")
        exit()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = f"{name} {status} {now}\n"
    with open('test_log.txt', 'a', encoding='utf-8') as f:
        f.write(total)


log_test("login_valid", "passed")
log_test("logout", "failed")

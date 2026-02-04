# Напиши программу, которая:
# читает его,
# выводит: "Базовый URL: https://example.com"
# изменяет timeout на 60,
# сохраняет обратно в файл.

with open("config.json", "a", encoding="utf-8") as f:
    read_te = f.read("base_url")
print(read_te)

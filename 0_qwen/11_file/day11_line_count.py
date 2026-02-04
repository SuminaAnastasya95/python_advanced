with open("input.txt", 'r', encoding='utf-8') as f:
    count = sum(1 for n in f)
print(f'в файле {count} строк')

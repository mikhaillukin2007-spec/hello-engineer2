octal_str = input("Введите число")

# Разбиваем на цифры
d1, d2, d3 = octal_str[0], octal_str[1], octal_str[2]

# Используем таблицу соответствий
table = "--- --x -w- -wx r-- r-x rw- rwx".split()

# Получаем индексы
result = table[int(d1)] + table[int(d2)] + table[int(d3)]

print(result)

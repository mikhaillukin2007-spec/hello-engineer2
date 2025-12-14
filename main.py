# Задаем сумму в рублях
rubles = float(input("Введите сумму в рублях: "))

# Актуальные курсы валют (примерные, нужно обновлять)
usd_rate = 79.71

# Конвертация
usd_amount = rubles / usd_rate

# Вывод результатов
print(f"Сумма в рублях: {rubles} руб.")
print(f"В долларах: {usd_amount:.2f} USD")

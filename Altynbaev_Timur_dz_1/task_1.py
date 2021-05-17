duration = int(input("Введите число в секундах: "))

if duration <= 60:
    print(f"{duration} секунд")
elif 60 < duration <= 3600:
    print(f"{duration // 60} минут, {duration % 60} секунд")
elif 3600 < duration <= 86400:
    print(f"{duration // 3600} часов, {duration % 3600 // 60} минут, {duration % 60} секунд")
else:
    print(f"{duration // 31104000} лет, "
          f"{duration % 31104000 // 2592000} месяцев, "
          f"{duration % 31104000 % 2592000 // 86400} дней, "
          f"{duration % 31104000 % 2592000  % 86400 // 3600} часов, "
          f"{duration % 31104000 % 2592000  % 86400 % 3600 // 60} минут, "
          f"{duration % 60} секунд")
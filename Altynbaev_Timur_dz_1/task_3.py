percent = int(input("Введите число от 0 до 20: "))

if percent == 1:
    print(f"{percent} процент")
elif 2 <= percent <= 4:
    print(f"{percent} процента")
elif 5 <= percent <= 20 or percent == 0:
    print(f"{percent} процентов")
else:
    print("Надо ввести число от 0 до 20")
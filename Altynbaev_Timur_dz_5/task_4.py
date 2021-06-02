import random

src = []
result = []


def randoming(long, diapason):
    for i in range(0, int(long)):
        num = random.randint(0, int(diapason))
        src.append(num)
    return src


def numbers():
    for i in range(0, len(src)):
        if src[i] == src[-1]:
            break
        elif src[i] < src[i + 1]:
            result.append(src[i + 1])
    return result


print(randoming(input("Укажите какой длинны должен быть список "),
                input("И в каком диапазоне будут рандомиться числа(отсчет идет от нуля) ")))

print(numbers())
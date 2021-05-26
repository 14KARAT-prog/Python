from random import choice  # Импортировал choice из модуля рандом

fun = []  # Создал пустой список
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adfectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, reruns):
    """
    Создаем цикл от 0 до n, где n - число которое задаем(может быть любым челым положительным числом)
    n - количество шуток.
    С помощью цикла проходим по раннее созданным спискам и
    с помощью функции choice достаем рандомные аргументы из списков,
    добавляя эти аргументы в зараннее созданный пустой список.
    Спустя n раз цикл заканчивает свою работу, на выходе получаем заполненный шутками список, который
    выводится на экран.
    """
    if reruns == 0:
        for i in range(0, n):
            a = choice(nouns)
            b = choice(adverbs)
            c = choice(adfectives)
            fun.append(a + " " + b + " " + c)
        print(fun)
    elif reruns == 1:
        for i in range(0, n):
            a = choice(nouns)
            b = choice(adverbs)
            c = choice(adfectives)
            while a in str(fun) or b in str(fun) or c in str(fun):
                a = choice(nouns)
                b = choice(adverbs)
                c = choice(adfectives)
            else:
                fun.append(a + " " + b + " " + c)
        print(fun)


get_jokes(5, 1)

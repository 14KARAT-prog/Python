words = {"zero": "ноль", "one": "один", "two": "два", "tree": "три", "four": "четыре", "five": "пять", "six": "шесть",
         "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate(num):
    words_keys = list(words.keys())
    words_values = list(words.values())
    for i in range(0, 11):
        if num == str(words_keys[i]):
            return words_values[i]
    return None


print(num_translate((str(input("Напишите число от 0 до 10 прописными буквами ").lower()))))

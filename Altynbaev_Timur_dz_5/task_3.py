tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
dict_1 = list(zip(tutors, klasses))
print(dict_1)


def generate():
    for i in dict_1:
        yield i


for m in generate():
    print(m)

# Если в tutors больше элементов используем zip_longest из модуля itertools

from itertools import zip_longest

tutors_new = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Хосэ']
klasses_new = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

dict_1_new = zip_longest(tutors_new, klasses_new)


def generate_new():
    for i in dict_1_new:
        yield i


for m in generate_new():
    print(m)

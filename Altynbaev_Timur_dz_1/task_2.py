list_1 = []
list_2 = []

for idx in range(0, 1000):
    if idx % 2 == 1:
        list_1.append(idx ** 3)

print(list_1)

sum_all = 0
for n, m in enumerate(list_1):
    sum = 0
    while m != 0:
        sum = sum + m % 10
        m = m // 10
    if sum % 7 == 0:
        sum_all = sum_all + list_1[n]

print(sum_all)

for n in list_1:
    list_2.append(n + 17)

sum_all = 0
for n, m in enumerate(list_2):
    sum = 0
    while m != 0:
        sum = sum + m % 10
        m = m // 10
    if sum % 7 == 0:
        sum_all = sum_all + list_2[n]

print(sum_all)
import collections

with open("nginx_logs.txt", "r", encoding="utf-8") as book:
    c = collections.Counter()
    for i in book:
        i = i.split()[0]
        c[i] += 1

print(f"Спаммер {c.most_common(1)[0][0]}, отправленно {c.most_common(1)[0][1]} запросов")

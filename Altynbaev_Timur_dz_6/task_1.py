with open("nginx_logs.txt", "r", encoding="utf-8") as book:
    content = ((cont.split()[0], cont.split()[5][1:], cont.split()[6]) for cont in book)
    for i in content:
        print(i)

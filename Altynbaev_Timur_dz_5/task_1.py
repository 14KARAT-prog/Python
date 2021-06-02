def my_gen(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            yield i


for m in my_gen(16):
    print(m)


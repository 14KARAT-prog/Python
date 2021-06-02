def my_gen(i):
    new_ = [i for i in range(1, i + 1) if i % 2 == 1]
    return new_


print(my_gen(11))

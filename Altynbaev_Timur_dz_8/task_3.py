def type_logger(func):
    def wrapper(*args):
        markup = func(*args)
        print({args: type(*args)})
        return markup

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)

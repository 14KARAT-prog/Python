names = {}


def thesaurus(*args):
    for i in args:
        n = i[0]
        if n in names:
            names[n] = names[n] + [i]
        else:
            names[n] = [i]

    return names


print(thesaurus("Hose", "Marina", "Marusa", "Olga", "Hooda", "Pasha", "Oleg", "Petr", "Polina"))

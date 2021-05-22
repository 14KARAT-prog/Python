Price = [43.24, 58, 81.9, 20, 7.89, 99.6, 67, 28.7, 73, 56.29, 48.5, 5]
Price.sort()

for i in Price:
    n, m = str(f"{i:.2f}").split(".")
    print(f"{n} руб {int(m):02d} коп,", end=" ")

Price_2 = sorted(Price, reverse=True)
print(Price_2)

print(Price_2[4], Price_2[3], Price_2[2], Price_2[1], Price_2[0])
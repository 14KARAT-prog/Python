List_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
List_2 = []

for i in List_1:
    if i.replace("+", "").isdigit():
        if i.isdigit():
            List_2.append(f"'{int(i):02}'")
        else:
            List_2.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        List_2.append(i)

print(List_2)
print(" ".join(List_2))
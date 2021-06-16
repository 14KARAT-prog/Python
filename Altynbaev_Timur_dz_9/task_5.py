class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


pen = Pen('Ручка')
pen.draw()
print(pen.title)

pencil = Pencil('Карандаш')
pencil.draw()
print(pencil.title)

handle = Handle('Маркер')
handle.draw()
print(handle.title)

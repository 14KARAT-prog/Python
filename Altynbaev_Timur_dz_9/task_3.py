class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя {self.name}, фамилия {self.surname}, должность {self.position}")

    def get_total_income(self):
        full_income = self._income["wage"] + self._income["bonus"]
        print(f"Полный доход {full_income} долларов")


a = Position('Hose', 'Rodrigas', 'Programmer', 1000, 500)
a.get_full_name()
a.get_total_income()

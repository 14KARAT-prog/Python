class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, standartMass=25, density=5):
        Mass = (self._width * self._length * standartMass * density) / 1000
        print(f"{self._width} м * {self._length} м * {standartMass} кг * {density} см = {Mass} т")


a = Road(20, 5000)
a.mass()

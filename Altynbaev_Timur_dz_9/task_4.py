import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("The car went")

    def stop(self):
        print("The car stopped")

    def turn(self):
        num = random.randint(1, 3)
        if num == 1:
            print("right turn")
        elif num == 2:
            print("left turn")
        elif num == 3:
            print("didn't turn anywhere")

    def show_speed(self):
        print(f"current vehicle speed {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Attention, overspeeding! {self.speed}, should not be more than 60")
        else:
            print(f"current vehicle speed {self.speed}")


class SportCar(Car):
    def MaxSpeed(self):
        print("accelerates to 300 km/h")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Attention, overspeeding! {self.speed}, should not be more than 40")
        else:
            print(f"current vehicle speed {self.speed}")


class PoliceCar(Car):
    def siren(self):
        num = random.randint(1, 2)
        if num == 1:
            print("siren on")
        else:
            print("siren off")


speed = random.randint(30, 100)

towncar = TownCar(speed, 'blue', 'Volkswagen golf', False)
towncar.show_speed()

sportcar = SportCar(speed, 'green', 'Lamborghini', False)
sportcar.MaxSpeed()

workcar = WorkCar(speed, 'white', 'Gazelle', False)
workcar.show_speed()

policecar = PoliceCar(speed, 'black', 'Ford Focus', True)
print(policecar.is_police)
policecar.siren()

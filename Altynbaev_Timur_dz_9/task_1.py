import time

class TrafficLight:
    __color = 'color'

    def running(self):
        while True:
            self.__color = 'red'
            print(self.__color)
            time.sleep(7)

            self.__color = 'yellow'
            print(self.__color)
            time.sleep(2)

            self.__color = 'green'
            print(self.__color)
            time.sleep(5)

            self.__color = 'yellow'
            print(self.__color)
            time.sleep(2)


a = TrafficLight()
print(a.running())
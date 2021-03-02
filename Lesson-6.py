# task 1
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running (self):
        print("запуск")
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(1)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()


# task 4


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Jon', 'Travolta', 'superman', 504548, 4444444545)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
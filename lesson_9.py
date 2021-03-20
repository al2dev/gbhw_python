import time


'''
    1. Создать класс TrafficLight (светофор).
    определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    продолжительность 
    первого состояния (красный) составляет 7 секунд, 
    второго (жёлтый) — 2 секунды, 
    третьего (зелёный) — на ваше усмотрение;
    
    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.
'''


class TrafficLight:
    def __init__(self):
        self.__start = None
        self.__color = None
        self.__colors = {'red': 7000,
                       'yellow': 2000,
                       'green': 5000}

    def running(self):
        if not self.__start:
            self.__start = time.time()

    def get_color(self):
        if self.__start:
            now_time = time.time()
            dif = (now_time - self.__start) * 1000
            ost = dif % sum(self.__colors.values())
            for color, delay in self.__colors.items():
                ost -= delay
                if ost < 0:
                    self.__color = color
                    break
            return self.__color


'''
    2. Реализовать класс Road (дорога).
    определить атрибуты: length (длина), width (ширина);
    значения атрибутов должны передаваться при создании экземпляра класса;
    атрибуты сделать защищёнными;
    определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
    проверить работу метода.
    Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__density = 0.025

    def get_weight(self, thickness):
        return self._length * self._width * self.__density * thickness


'''
    3. Реализовать базовый класс Worker (работник).
    определить атрибуты: name, surname, position (должность), income (доход);
    
    последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
    оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
    и дохода с учётом премии (get_total_income); 
    проверить работу примера на реальных данных: 
    создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''


class Worker:
    income = {"wage": 1000, "bonus": 150}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = Worker.income


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return sum(self._income.values())


'''
    4. Реализуйте базовый класс Car.
    у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). 
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed. 
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car go')

    def stop(self):
        print('Car stop')

    def turn(self, direction):
        print('Car turn: ', str(direction))

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Over speed:', self.speed)
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Over speed:', self.speed)
        else:
            super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


'''
    5. Реализовать класс Stationery (канцелярская принадлежность).
    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером')


if __name__ == '__main__':
    # 1 task
    print('\n')
    print('Task 1')
    tl = TrafficLight()
    tl.running()
    for n in range(15):
        print(tl.get_color())
        time.sleep(1)

    # 2 task
    print('\n')
    print('Task 2')
    r = Road(5, 300)
    print(r.get_weight(0.007), 'т', end='\n\n')

    # 3 task
    print('\n')
    print('Task 3')
    p = Position('john', 'Doe', 'manager')
    print(p.get_full_name())
    print(str(p.get_total_income()))

    # 4 task
    print('\n')
    print('Task 4')
    print('town cars')
    tc10 = TownCar(10, 'white', 'just car')
    tc10.show_speed()
    tc100 = TownCar(100, 'white', 'just car')
    tc100.show_speed()

    print('police cars')
    pc10 = TownCar(10, 'black', 'police car')
    pc10.show_speed()
    pc100 = TownCar(100, 'black', 'police car')
    pc100.show_speed()


    # 5 task
    print('\n')
    print('Task 5')
    pn = Pen('Pen')
    pnc = Pencil('Pencil')
    mrk = Handle('Handle')

    pn.draw()
    pnc.draw()
    mrk.draw()

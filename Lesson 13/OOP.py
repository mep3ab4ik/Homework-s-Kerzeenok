"""1. Реализовать абстрактный класс машины (придумайте какие методы у машины есть,
какие нужно у всех дочерних классов переопределять, а какие будут общие с готовой реализацией)
2. Реализовать несколько классов разных марок машин, наследуемых от базовой машины.
Переопределить абстрактные методы, свойства. Придумать новые методы, которые есть только в конкретных марках машин.
3. Реализовать класс абстрактный класс самолета.
Должно быть как минимум один или несколько одноименных атрибутов класса машины. Тоже самое из п.1
4. Реализовать несколько классов разных марок самолетов. Тоже самое из п.2
5. Создать несколько экземпляров каждой машины, каждого самолета,
вызвать различные методы у этих объектов. «Поиграться», скажем так. А затем сделать коллекцию из этих объектов и
через цикл пройтись по каждому из этих объектов и вызвать те методы, которые есть во всех классах."""


class Car:
    tire: int = 4
    door: int = 5
    color: str = "Black"
    car: str = "car"


    def drive(self, speed: int = 0):
        drive_speed = f"The {self.car} road with {speed} km/h"
        return drive_speed

    def info(self):
        return f"The {self.car} have {self.tire} tires, {self.door} doors. The color a car it {self.color}"


class CarBMW(Car):

    tire: int = 5
    color: str = "Grey"
    car: str = "BMW"

    def check(self, lamp:int = 0):
        return f"Ламчока чек загорелась {lamp} раз"


class CarMers(Car):

    door: int = 3
    car: str = "Mers"

    def years(self, year):
        return f"{self.car} {year} года выпуска"


car = Car()
bwm = CarBMW()
mers = CarMers()
mers.color = "Pink"


class Plane:
    speed: int = 400
    pilot: int = 2
    color: str = "Grey"

    def speed_plane(self):
        return f"The speed plane is {self.speed} km/h"

    def info(self):
        return f"The plane have a {self.pilot} pilots and color {self.color}"

class SY29(Plane):
    speed: int = 800
    pilot: int = 1
    weapon: str = "Minigan"

    def weapon_plane(self):
        return f"The plane have weapon - {self.weapon}"


class PrivatePlane(Plane):
    pilot: int = 3
    side_place: int = 12

    def place(self):
        return f"The plane have {self.side_place} side place"

plane = Plane()
sy = SY29()
private = PrivatePlane()

cars = [car, bwm, mers]
fly = [plane, sy, private]

for i in cars:
    print(i.info())
    if i == car:
        print(i.drive(150))
    elif i == bwm:
        print(i.drive(200))
        print(i.check(10))
    elif i == mers:
        print(i.drive(250))
        print(i.years(2000))

print()
for i in fly:
    print(i.info())
    print(i.speed_plane())
    if i == sy:
        print(i.weapon_plane())
    elif i == private:
        print(i.place())

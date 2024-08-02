from abc import ABC, abstractmethod


# Основной класс MeansOfTransport
class MeansOfTransport:
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def show_color(self):
        print(f"The color of the transport is: {self._color}")

    def show_brand(self):
        print(f"The brand of the transport is: {self._brand}")


# Класс Car, наследующий MeansOfTransport
class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels
        self._protected_variable = "Protected"
        self.__private_variable = "Private"
        self.public_variable = "Public"

    @classmethod
    def show_car_drive(cls):
        print(f"Car drive: {cls.car_drive}")

    def __str__(self):
        return f"Car: {self._brand}, Color: {self._color}, Wheels: {self.wheels}"

    def __repr__(self):
        return f"Car({self._brand}, {self._color}, {self.wheels})"

    def __eq__(self, other):
        if isinstance(other, Car):
            return (self._brand, self._color, self.wheels) == (other._brand, other._color, other.wheels)
        return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.wheels < other.wheels
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Car):
            return self.wheels <= other.wheels
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.wheels > other.wheels
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Car):
            return self.wheels >= other.wheels
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Car):
            return not self.__eq__(other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Car):
            return self.wheels + other.wheels
        return NotImplemented

    def __len__(self):
        return self.wheels

    def __call__(self):
        self.show_color()
        self.show_brand()


# Класс Moped, наследующий MeansOfTransport
class Moped(MeansOfTransport):
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    @staticmethod
    def calculate_time(distance, max_speed):
        if max_speed == 0:
            return float('inf')
        return distance / max_speed


# Класс Calculator
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


# Класс StringCalculator, наследующий Calculator
class StringCalculator(Calculator):
    @staticmethod
    def add(a, b):
        return str(a) + str(b)


# Абстрактный класс Animals
class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass


# Класс Cat, наследующий Animals
class Cat(Animals):
    def voice(self):
        print("Meow")


# Шаблон Singleton для класса Dog
class Dog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Dog, cls).__new__(cls)
        return cls._instance

    def __init__(self, name, age):
        if not hasattr(self, 'initialized'):
            self.name = name
            self.age = age
            self.initialized = True

    def __str__(self):
        return f"Dog: {self.name}, Age: {self.age}"

    def bark(self):
        print("Woof!")


# Класс для работы со списком людей
class PeopleList:
    def __init__(self):
        self.people = []

    def add_person(self, name):
        self.people.append(name)

    def __iter__(self):
        return iter(self.people)


# Класс с логированием изменений атрибутов
class LoggedAttributes:
    def __init__(self, attr1, attr2, attr3):
        self._attr1 = attr1
        self._attr2 = attr2
        self._attr3 = attr3

    @property
    def attr1(self):
        return self._attr1

    @attr1.setter
    def attr1(self, value):
        print(f"Changing attr1 from {self._attr1} to {value}")
        self._attr1 = value

    @property
    def attr2(self):
        return self._attr2

    @attr2.setter
    def attr2(self, value):
        print(f"Changing attr2 from {self._attr2} to {value}")
        self._attr2 = value

    @property
    def attr3(self):
        return self._attr3

    @attr3.setter
    def attr3(self, value):
        print(f"Changing attr3 from {self._attr3} to {value}")
        self._attr3 = value


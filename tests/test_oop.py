# test_transport.py
import pytest
from task_oop import ooptesting


def test_means_of_transport():
    transport = ooptesting.MeansOfTransport("Toyota", "Red")
    assert transport.get_color() == "Red"
    assert transport.get_brand() == "Toyota"
    transport.set_color("Blue")
    transport.set_brand("Honda")
    assert transport.get_color() == "Blue"
    assert transport.get_brand() == "Honda"


def test_car():
    car1 = ooptesting.Car("Toyota", "Red", 4)
    car2 = ooptesting.Car("Honda", "Blue", 4)
    car3 = ooptesting.Car("Toyota", "Red", 4)

    assert str(car1) == "Car: Toyota, Color: Red, Wheels: 4"
    assert repr(car1) == "Car(Toyota, Red, 4)"
    assert car1 == car3
    assert car1 != car2
    assert car1 <= car2
    assert not car1 < car2
    assert car1 + car2 == 8
    assert len(car1) == 4
    car1()


def test_moped():
    moped = ooptesting.Moped("Yamaha", "Black", 2)
    assert moped.wheels == 2
    assert moped.calculate_time(100, 50) == 2.0
    assert moped.calculate_time(100, 0) == float('inf')


def test_calculator():
    assert ooptesting.Calculator.add(2, 3) == 5


def test_string_calculator():
    assert ooptesting.StringCalculator.add("2", "3") == "23"


def test_cat():
    cat = ooptesting.Cat()
    cat.voice()


def test_dog_singleton():
    dog1 = ooptesting.Dog("Buddy", 3)
    dog2 = ooptesting.Dog("Max", 5)
    assert dog1 is dog2
    assert dog1.name == "Buddy"
    assert dog2.name == "Buddy"


def test_people_list():
    people_list = ooptesting.PeopleList()
    people_list.add_person("Alice")
    people_list.add_person("Bob")
    assert list(people_list) == ["Alice", "Bob"]


def test_logged_attributes(capsys):
    attrs = ooptesting.LoggedAttributes("value1", "value2", "value3")
    attrs.attr1 = "new_value1"
    attrs.attr2 = "new_value2"
    attrs.attr3 = "new_value3"
    captured = capsys.readouterr()
    assert "Changing attr1 from value1 to new_value1" in captured.out
    assert "Changing attr2 from value2 to new_value2" in captured.out
    assert "Changing attr3 from value3 to new_value3" in captured.out

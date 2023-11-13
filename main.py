"""import Classes and pytest"""
from candy import Candy, Dinner, Type
import pytest


@pytest.fixture(name="sample_candies_test")
def sample_candies():
    """defining candies"""
    candy1 = Candy("Snickers", 50, 2, 1.5, Type.BAR)
    candy2 = Candy("M&Ms", 30, 3, 1.0, Type.BUTTON)
    candy3 = Candy("Popcorn Candy", 40, 1, 2.0, Type.POPCORN)
    candy4 = Candy("Bubble Gum", 10, 5, 0.5, Type.GUM)
    return [candy1, candy2, candy3, candy4]


def test_ate_function():
    """eating candies"""
    candy = Candy("Test Candy", 100, 3, 1.0, Type.BAR)
    assert candy.ate() == "What delicious candies!"


def test_find_the_most_expensive_candies(sample_candies_test):
    """find the most expensive candy"""
    dinner_price = Dinner("Monday", "18:00", sample_candies_test)
    most_expensive_candies = dinner_price.find_the_most_expensive_candies()
    assert len(most_expensive_candies) == 3
    assert most_expensive_candies[0].price >= most_expensive_candies[1].price
    assert most_expensive_candies[1].price >= most_expensive_candies[2].price


def test_find_the_most_by_mass(sample_candies_test):
    """find_the_most_by_mass candy"""
    dinner_mass = Dinner("Tuesday", "20:00", sample_candies_test)
    most_massive_candy = dinner_mass.find_the_most("mass")
    assert most_massive_candy.name == "Snickers"


def test_find_the_most_by_amount(sample_candies_test):
    """find_the_most_by_amount candy"""
    dinner_amount = Dinner("Wednesday", "19:30", sample_candies_test)
    most_amount_candy = dinner_amount.find_the_most("amount")
    assert most_amount_candy.name == "Bubble Gum"


candies = [
    Candy("Chocolate bar", 100000000, 10, 10, Type.BAR),
    Candy("Gummy bear", 50, 27, 14, Type.GUM),
    Candy("Popcorn", 100, 10, 2, Type.POPCORN),
    Candy("Button", 10, 100, 1, Type.BUTTON),
]

dinner = Dinner("Monday", "12:00", candies)

print(dinner)
print(dinner.find_the_most("amount"))
print(dinner.find_the_most_expensive_candies())

print(candies[0].ate())
print(candies[1].ate())
print(candies[2].ate())

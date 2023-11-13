"""import Enum"""
from enum import Enum


class Type(Enum):
    """Enum"""
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4


class Candy:
    """class Candy"""
    def __init__(self, name, mass, amount, price, tp):
        """init attributes"""
        self.name = name
        self.mass = mass
        self.amount = amount
        self.price = price
        self.type = tp

    def ate(self):
        """eating"""
        if self.mass * self.amount > 2000:
            result = "You’re on a diet!"
        else:
            result = "What delicious candies!"
        return result

    def __repr__(self):
        """stringing"""
        return f"{self.name}, {self.mass}, {self.amount}, {self.price}"


class Dinner:
    """not breakfast"""
    def __init__(self, day, time, candies):
        self.day = day
        self.time = time
        self.candies = candies

    def __repr__(self):
        """stringing"""
        return f"{self.day}, {self.time}, {self.candies}"

    def find_the_most_expensive_candies(self):
        """finding some shit"""
        most_expensive_candies = sorted(self.candies, key=lambda candy: candy.price,
                                        reverse=True)[:3]
        return most_expensive_candies

    def find_the_most(self, attribute):
        """finding another shit"""
        most_expensive_candies = sorted(self.candies, key=lambda candy: getattr(candy, attribute),
                                        reverse=True)
        return most_expensive_candies[0]

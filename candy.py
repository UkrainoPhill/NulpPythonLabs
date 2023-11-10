from enum import Enum


class Type(Enum):
    BAR = 1
    BUTTON = 2
    POPCORN = 3
    GUM = 4


class Candy:
    def __init__(self, name, mass, amount, price, tp):
        self.name = name
        self.mass = mass
        self.amount = amount
        self.price = price
        self.type = tp

    def ate(self):
        if self.mass * self.amount > 2000:
            result = "You’re on a diet!"
        else:
            result = "What delicious candies!"
        return result

    def __repr__(self):
        return f"{self.name}, {self.mass}, {self.amount}, {self.price}"


class Dinner:
    def __init__(self, day, time, candies):
        self.day = day
        self.time = time
        self.candies = candies

    def __repr__(self):
        return f"{self.day}, {self.time}, {self.candies}"

    def find_the_most_expensive_candies(self):
        most_expensive_candies = sorted(self.candies, key=lambda candy: candy.price, reverse=True)[:3]
        return most_expensive_candies

    def find_the_most(self, attribute):
        most_expensive_candies = sorted(self.candies, key=lambda candy: getattr(candy, attribute), reverse=True)
        return most_expensive_candies[0]

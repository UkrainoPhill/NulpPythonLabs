from enum import Enum
import logging


def logged(exception: Exception, mode: str = "console"):
    def wrapper(func):

        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
                    logging.error(e)
                    raise
                else:
                    print(f"Error: {e}")
            except (AteException, NotExistingAttributteException) as e:
                if mode == "console":
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
                    logging.error(e)
                    raise
                else:
                    print(f"Error: {e}")

            finally:
                if mode == "file":
                    logging.shutdown()

        return inner

    return wrapper


class AteException(Exception):

    def __init__(self, candy):
        super().__init__(f"pls, write str")


class NotExistingAttributteException(Exception):

    def __init__(self, candy):
        super().__init__(f"pls, write mass, amount or price")

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

    def __repr__(self):
        return f"{self.name}, {self.mass}, {self.amount}, {self.price}"

    @logged(AteException, mode = 'console')
    def ate(self):
        if isinstance(self.mass or self.amount, str):
            raise AteException(self)
        if self.mass * self.amount > 2000:
            result = "You’re on a diet!"
        else:
            result = "What delicious candies!"
        return result


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

    @logged(NotExistingAttributteException, mode='console')
    def find_the_most(self, attribute):
        if attribute not in ["mass", "amount", "price"]:
            raise NotExistingAttributteException(self)
        most_expensive_candies = sorted(self.candies, key=lambda candy: getattr(candy, attribute), reverse=True)
        return most_expensive_candies[0]

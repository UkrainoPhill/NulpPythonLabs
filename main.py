from candy import Candy, Dinner, Type


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

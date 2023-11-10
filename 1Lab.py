import math

movie = "Oppenheimer"
print(movie)

is_employee = True
is_employer = False
is_sunny = False
is_raining = True

print(is_employee and is_employer)
print(is_employee or is_employer)
print(is_employee is not is_employer)

print(is_sunny is not is_raining)

x = 2.531
y = 0.193

a = ((y*y*y)*(x*y)**(1/3)) + (y*math.sin(x*y)) - (math.e ** (-x * y) * (math.cos(x * y))) + (7.1 / (x * y))
print(a)

import math

print("#############################A#############################")

h = 0.2
x = 2
b = 5.1
a = 2

while x < b:
    if x < 3:
        print(round(x, 2), "\t", 1 / math.tan(x + 1 / math.cos(x ** (-2))))
    elif (x >= 3) and (x < 4):
        print(round(x, 2), "\t", math.log10(math.log(x, math.e) + math.log(x, 3)))
    elif x >= 4:
        print(round(x, 2), "\t", math.cos(5 * x * x))
    x += h

print("#############################B#############################")

x = 0.5
n = 1
S = 1
h = 0.05
su = 1

while x < 0.91:
    while math.fabs(su) >= 0.001:
        su = ((2 * n - 1) / (2 * n) * (2 * n + 1)) * x ** (2 * n + 1)
        S = math.pi / 2 - x - su
        n += 1
    print(round(x, 2), "\t", S)
    x += h
    n = 1
    su = 1
    S = 1

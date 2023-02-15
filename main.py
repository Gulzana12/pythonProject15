import math

x = float(input("x="))
y = 1
g = 1
s = 0

if x < -1:
    e = 0.001
    while y > e:
        y = - math.pi/2 - 1 / g*pow(x,-g)
        g += 2
        s += y
    print("Zhauap=", s)
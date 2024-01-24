import math

# 3 Вариант

x = 3.74 * math.pow(10, -2)
y = -0.825
z = 0.16 * math.pow(10, 2)

s = 1 + math.pow(math.sin(x + y), 2)
s /= math.fabs(x - (2 * y) / (1 + math.pow(x, 2) * math.pow(y, 2)))
s *= math.pow(x, math.fabs(y))
s += math.pow(math.cos(math.atan(1 / z)), 2)

print('s = {0:.5f}'.format(s))

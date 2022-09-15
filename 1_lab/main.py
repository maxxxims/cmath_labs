from math import pi, e
import matplotlib.pyplot as plt
N = int(input())
y = [0] * N

y[0] = y[1] = pi / (e + 17)

for i in range(2, N):
    y[i] = pi - 12*y[i-1] -5*y[i-2]

print(y)
plt.scatter([i for i in range(len(y))], y)
plt.grid()
plt.show()
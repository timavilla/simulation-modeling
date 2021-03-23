import matplotlib.pyplot as plt
from model import SpaceCraft 
from integrator import tRungeKutta 


SpaceCraft1 = SpaceCraft()

vector = [31200000.0, 31200000.0, 0.0, -1700.0, 1200.0, -1900.0]
RungeKutta = tRungeKutta(0, 200000, 1)

tt = [i for i in range(RungeKutta.tk//RungeKutta.h)]
x = []
y = []
z = []


for i in range (RungeKutta.t0, RungeKutta.tk):
    print('\r', end='')
    print('Progress: %.1f' % (i/RungeKutta.tk*100), '%', end='')
    RungeKutta.oneStep(SpaceCraft1, vector)
    x.append(vector[0])
    y.append(vector[1])
    z.append(vector[2])
    RungeKutta.t0 += RungeKutta.h

with open('x.txt', 'w') as fx, open('y.txt', 'w') as fy, open('z.txt', 'w') as fz:
    for i in range(len(x)):
        fx.write(str(x[i]) + '\n')
        fy.write(str(y[i]) + '\n')
        fz.write(str(z[i]) + '\n')


plt.title('Зависимость координат от времени')
plt.plot(tt, x, label='x')
plt.plot(tt, y, label='y')
plt.plot(tt, z, label='z')
plt.xlabel('t')
plt.legend()
plt.savefig('result.png')
plt.show()


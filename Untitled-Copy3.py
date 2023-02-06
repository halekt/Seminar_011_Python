#!/usr/bin/env python
# coding: utf-8

# # In[ ]:


# Задача. Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3 + 5x^2 + 10x - 30

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

a, b, c, d, i = -12, 18, 5, 10, -30

limit = 10
step = 0.001

x = np.arange(-limit, limit, step)


def func(x):
    return  a*x**4*np.sin(np.cos(x)) - b*x**3 + c*x**2 + d*x - i


def take_roots(a, b, c, d, i) -> tuple:
    discr = (b**2 - 4*a*b)
    if discr > 0:
        x1 = (-b + discr**0.5)/(2*a)
        x2 = (-b - discr**0.5)/(2*a)
        return round(x1, 3), round(x2, 3)
    elif discr == 0:
        x = -b/(2*a)
        return round(x, 4 )
    else:
        return(None, )

roots = take_roots(a, b, c, d, i)
print(roots)

min_y = min(func(x))
min_x = take_roots(a, b, c, d, i - min_y )[0]
print(min_x, min_y)


x_down_pos = np.arange(-limit, min(roots), step)
x_down_neg = np.arange(min(roots),min_x, step)
x_up_neg = np.arange(min_x, max(roots), step)
x_up_pos = np.arange(max(roots),limit, step)


plt.rcParams['lines.linestyle'] = '-'
plt.plot(x_down_pos, func(x_down_pos), 'b', label = 'Убывание больше 0')
plt.plot(x_up_pos, func(x_up_pos), 'r', label = 'Возрастание больше 0')

plt.rcParams['lines.linestyle'] = '-.'
plt.plot(x_down_neg, func(x_down_neg), 'b' , label = 'Убывание меньше 0')
plt.plot(x_up_neg, func(x_up_neg), 'r' , label = 'Возрастание меньше 0')

#plt.plot(x_up, func(x_up), 'r')
plt.plot(roots[0], 0, 'yo' , label = f'Корни ({roots[0]} , {roots[1]})')
plt.plot(roots[1], 0, 'yo')
plt.plot(min_x, min_y, [0], 'gx' , label = f'Экстремум функции ({min_x} , {min_y})')
plt.legend()
plt.grid ()
plt.show()














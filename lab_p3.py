import numpy as np
import math

x1 = 1.0
xn = 5.0
deltax = 0.4
b = 0.37

print("Вычисление значений функции с использованием цикла while")
print(f"{'x':^10} {'y':^15}")

x = x1
while x <= xn:
    y = (math.e**(2 * x) - (math.e**(b * x)) / x**6 * (1 + x**(1/2)))
    print(f"{x:^10.2} {y:^15.6e}")
    
    x += deltax

print("Вычисление значений функции с использованием цикла for")
print(f"{'x':^10} {'y':^15}")

x = x1
for x in np.arange(x1, xn+deltax, deltax):  
    y = (math.e**(2 * x) - (math.e**(b * x)) / x**6 * (1 + x**(1/2)))
    print(f"{x:^10.2} {y:^15.6e}")
    
    x += deltax

import math

def c_vichilnie(x, y, k):
 ## выбор функции
    if k == 1:
        f_x = math.cos(y)
    elif k == 2:
        f_x = math.e**(math.sin(x))
    elif k == 3:
        f_x = math.log(y)
    else:
        print("Неправильный выбор функции. Введите 1, 2 или 3.")
        return None
    
    xy_abs = abs(x*y)
    
## вычесление функции и вывод
    if xy_abs > 12:
        c = math.log(abs(f_x))
        print("Выбрана первая ветвь: c = ln(|f(x)|)")

    elif xy_abs < 12:
        c = abs(f_x)**(1/3) + math.e**(f_x)
        print("Выбрана вторая ветвь: c = (|f(x)|)^(1/2) + e^(f(x))")

    else:
        c = ((f(x))**2)**(1/3) + y**(1/2)
        print("Выбрана третья ветвь: с = ((f(x))^2)^(1\3) + y^(1\2)")
        
    return c

x = float(input("Введите x: "))
y = float(input("Введите y: "))
k = int(input("Выберите функцию f(x): 1 - cos(y), 2 - e^(sin(x)), 3 - ln(y): "))

c = c_vichilnie(x, y, k)
print(f"Результат: c = {c}")


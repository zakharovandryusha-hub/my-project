import time      # для измерения времени выполнения
import sys       # для настройки системных параметров Python
import psutil    # для получения информации о процессе (память)

N = int(input("-->"))
start_time = time.time()    # запоминаем момент начала работы
sys.set_int_max_str_digits(0) # 0 = без ограничений снятие ограничения на длину целых чисел
if N%2 != 0 and N%5 != 0:   # Репьюнит (число из одних единиц: 1, 11, 111...) делится на N только если N не делится на 2 и на 5 — иначе решений нету
    n = 0
    e = 0
    while True:
        n=(n*10+1)%N #конструкция позволяет нам не хранмить огромное число целиком
        e +=1
        if n == 0:  # остаток = 0, значит нашли делитель
            result = '1'*e
            break
else:
    result = 'NO'
# замер времени и памяти
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.4f} секунд")
process = psutil.Process()
size_mem = process.memory_info().rss/1024/1024
print(f"Выделено памяти: {size_mem:.4f} Mb")
print(result)

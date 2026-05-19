import numpy as np
import time
from scipy.linalg.blas import cgemm

n = 2048

# генерируем матрицы
A = (np.random.rand(n, n) + 1j * np.random.rand(n, n)).astype(np.complex64)
B = (np.random.rand(n, n) + 1j * np.random.rand(n, n)).astype(np.complex64)

c = 2 * n**3  # сложность
print(f"сложность c = {c}")

# вариант 1 - по формуле
print("вариант 1...")
C1 = np.zeros((n, n), dtype=np.complex64)
t = time.time()
for i in range(n):
    for j in range(n):
        for k in range(n):
            C1[i][j] += A[i][k] * B[k][j]
t1 = time.time() - t
print(f"время: {t1} сек")
print(f"производительность: {c / (t1 * 10**6)} MFlops")

# вариант 2 - настоящий cblas_cgemm через scipy.linalg.blas
print("вариант 2...")
t = time.time()
C2 = cgemm(1.0, A, B)  # cgemm(alpha, A, B) => alpha * A @ B
t2 = time.time() - t
print(f"время: {t2} сек")
print(f"производительность: {c / (t2 * 10**6)} MFlops")

# вариант 3 - оптимизированный (блоками)
print("вариант 3...")
block = 64
C3 = np.zeros((n, n), dtype=np.complex64)
t = time.time()
for i in range(0, n, block):
    for j in range(0, n, block):
        for k in range(0, n, block):
            C3[i:i+block, j:j+block] += A[i:i+block, k:k+block] @ B[k:k+block, j:j+block]
t3 = time.time() - t
print(f"время: {t3} сек")
print(f"производительность: {c / (t3 * 10**6)} MFlops")

print(f"\nвариант 3 это {c / (t3 * 10**6) / (c / (t2 * 10**6)) * 100:.1f}% от варианта 2")

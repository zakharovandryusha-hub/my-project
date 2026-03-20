import math

x = float(2.45)
y = float(-0.423 * 10**(-2))    
z = float(1.232 * 10**(3))

S = (x**(2*y) + math.e**(y-1)) / (1 + x * abs(y - math.tan(z))) +10 * x**(1/3) - math.log(z)

print(x)
print(y)
print(z)
print(S)

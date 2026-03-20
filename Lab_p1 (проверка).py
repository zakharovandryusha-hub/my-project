import math

x = 27
y = 1  
z = 180

S = (x**(2*y) + (math.e**(y-1))) / (1 + (x * abs(y - math.tan(z)))) + (10 * x**(1/3)) - math.log(z)
faq = (x**(2*y))
lk = (math.e**(y-1))
rt = faq + lk
wq = 1 + (x * abs(y - math.tan(z)))
rq = ((x**(2*y)) + (math.e**(y-1))) / wq
ty = rq + 10 * (x**(1/3))
qs = ty - math.log(z)
print(S)

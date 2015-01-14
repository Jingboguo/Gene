
k = range (11)
import random 
m = 0
n = 0
p1 = random.choice(k[((m * 10) + n):((m * 10) + n + 10)])
index = k.index(p1)
del k[index]
p2 = random.choice(k[((m * 10) + n):((m * 10) + n + 9)])
print p1
print p2
print k
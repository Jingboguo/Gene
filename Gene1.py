# define 10 parents
import random 

k = range (110)
m = 0
while m <= 9: 
	n = 0
	while n <= 9:
		p1 = random.choice(k[(m * 10):((m * 10) + 10)])
		index = k.index(p1)
		del k[index]
		p2 = random.choice(k[(m * 10):((m * 10) + 9)])
		k.insert(index, p1)
		if m == 0:
			p1 = [p1]
			p2 = [p2]
		#print p1
		#print p2
		pp1 = p1[:]
		pp1.extend(p2)
		#print pp1
		k[((m + 1) * 10) + n] = pp1
		n = n + 1
	print "This is ", m ,"iterarion"
	print k[((m + 1) * 10):(m + 1) * 10 + 10]
		

	m = m + 1

# Count process

c = [0] * 10 #Tao: Bug here c = range(10)
for l in range (10): 
	h = 100
	while h < 110:
		c[l] = c[l] + k[h].count(l)
		h = h + 1

	l = l + 1

print c 








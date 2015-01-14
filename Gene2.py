# define 10 parents
import random 

k = range (10000)
p = range (10000)
m = 0
while m < 10000: 
	n = 0
	while n < 10000:
		p1 = random.choice(p)
		index = p.index(p1)
		del p[index]
		p2 = random.choice(p)
		p.insert(index, p1)
		if m == 0:
			p1 = [p1]
			p2 = [p2]
		#print p1
		#print p2
		pp1 = p1[:]
		pp1.extend(p2)
		#print pp1
		k[n] = pp1
		n = n + 1
	p = k[:]	

	print "This is kids of ", m ,"iterarion"
	print k
		

	m = m + 1

# Count process

c = [0] * 10000 #Tao: Bug here c = range(10)
for l in range (10000): 
	h = 0
	while h < 10000:
		c[l] = c[l] + k[h].count(l)
		h = h + 1

	l = l + 1

print c 








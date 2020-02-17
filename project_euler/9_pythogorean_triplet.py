values = [(x,y,z) for x in range(1, 501) for y in range(x,501) for z in range(y,501) if y**2+x**2 == z**2]

for i in values:
	sm = i[0] + i[1] + i[2]
	if sm == 1000:
		break
print (i)
print (i[0]*i[1]*i[2])
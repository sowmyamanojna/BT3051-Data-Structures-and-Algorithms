def coins(c, money):
	if money == 0:
		return 0
	else:
		vals = []
		for i in range(len(c)):
			print ("amount reduced:", c[i])
			print ("new amount:", money-c[i])
			vals.append(1+coins(c, money-c[i]))
			print (vals)
		return min(vals)

def get_coins(c, money):
	for i in range(len(c)):
		if money-c[i] >= 0:
			return 1+coins(money-c[i])

curr = [1, 4, 5]
money = 8
print (coins(curr, money))
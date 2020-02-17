def mul_3_5(n):
	div = [i for i in range(1, n) if i%3 == 0 or i%5 == 0]
	
	return sum(div)

print(mul_3_5(10))
print(mul_3_5(1000))
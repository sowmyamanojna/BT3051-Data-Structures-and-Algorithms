def coin_change(currency, money):
	if money in currency:
		return 1
	elif money == 0:
		return 0
	else:
		values = []
		for i in range(len(currency)-1, -1, -1):
			curr = currency[i]
			if money-curr >= 0:
				values.append(1+coin_change(currency, money-curr))
		return min(values)

money = int(input("Amount: "))
currency = list(map(int, input("Enter currency: ").strip().split()))
print (coin_change(currency, money))
def CoinChange(denom, amount):
	array = [0]*(amount+1)
	for i in range(1, amount+1):
		poss = []
		for cur in denom:
			if i-cur >= 0:
				poss.append(array[i-cur]+1)
				print(poss)
		array[i] = min(poss)


	print(poss)

	return array[-1]

denom = 
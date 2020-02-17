def find_largest_palindrome():
	max_val = 1000
	for x in range(999, 99, -1):
		for y in range(999, 99, -1):
			if str(x*y) == str(x*y)[::-1]:
				if max_val < x*y:
					max_val = x*y

	return max_val

print(find_largest_palindrome())
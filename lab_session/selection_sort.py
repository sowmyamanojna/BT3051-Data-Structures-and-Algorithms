def selection_sort(value):
	n = len(value)
	for i in range(n-1):
		loc = i
		for j in range(i+1, n):
			if value[j] < value[loc]:
				loc = j
		if loc != i:
			value[i], value[loc] = value[loc], value[i]
		print(value)

	return value

values = [6, 5, 3, 1, 8, 7, 2, 4]
print (values)
values = selection_sort(values)

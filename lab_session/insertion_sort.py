def insertion_sort(value):
	n = len(value)
	for i in range(n-1):
		j = i+1
		if value[i+1] < value[i]:
			while j>=1 and value[j]<value[j-1]:
				value[j-1], value[j] = value[j], value[j-1]
				j -= 1
		print (value)

	return value

values1 = [6, 5, 3, 1, 8, 7, 2, 4]
print (values1)
values = insertion_sort(values1)

print()

values2 = list(range(8, 0, -1))
print(values2)
values = insertion_sort(values2)

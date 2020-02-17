def bubble_sort(values):
	n = len(values)
	for i in range(n-1):
		sort = False
		for j in range(n-1-i):
			if values[j]>values[j+1]:
				sort = True
				values[j], values[j+1]= values[j+1], values[j]

		if sort == False:
			break

		print (values)

values = [6, 5, 3, 1, 8, 7, 2, 4]
print (values)
values = bubble_sort(values)
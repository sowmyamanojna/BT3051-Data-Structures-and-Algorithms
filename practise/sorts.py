def bubble_sort(a):
	n = len(a)
	for i in range(n-1):
		sort = False
		for j in range(n-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				sort = True

		for k in a:
			print(k, end = " ")
		print ()

		if not sort:
			break

	return a


def selection_sort(a):
	n = len(a)
	for i in range(n-1):
		min_pos = i
		for j in range(i+1, n):
			if a[min_pos] > a[j]:
				min_pos = j
		a[i], a[min_pos] = a[min_pos], a[i]

		for k in a:
			print (k, end = " ")
		print ()

	return a


def insertion_sort(a):
	n = len(a)
	print (a)
	for i in range(1, n):
		pos = i
		for j in range(i-1, -1, -1):
			if a[i] < a[j]:
				pos = j
		a[pos], a[pos+1:i+1] = a[i], a[pos:i]

		for k in a:
			print (k, end = " ")
		print ()

	return a


def merge_sort(a):
	n = len(a)
	if n == 1:
		print(a)
		return a
	elif n % 2 == 0:
		print (a)
		return merge(merge_sort(a[:n//2]), merge_sort(a[n//2:]))
	else:
		print (a)
		return merge(merge_sort(a[:(n+1)//2]), merge_sort(a[(n+1)//2:]))

def merge(a, b):
	n = len(a)
	m = len(b)
	i = 0
	j = 0
	new = []
	while i<n and j<m:
		if a[i] < b[j]:
			new.append(a[i])
			i += 1
		elif b[j] < a[i]:
			new.append(b[j])
			j += 1
		else:
			new.append(a[i])
			new.append(b[j])
			i += 1
			j += 1
	if i<n:
		new.extend(a[i:])
	elif j<m:
		new.extend(b[j:])

	print (new)

	return new


def quicksort(a):
	n = len(a)
	if n <= 1:
		return a

	else:
		p_pos = n-1
		p = a[n-1]
		smaller = []
		larger = []

		for i in range(n-1):
			if a[i] <= p:
				smaller.append(a[i])
			elif a[i] > p:
				larger.append(a[i])

		new = []
		new.extend(quicksort(smaller))
		new.append(p)
		new.extend(quicksort(larger))

		print(new)

		return new


a = [6, 5, 3, 1, 8, 7, 2, 4]
print ("quicksort")
print (quicksort(a))
print(a)
# print ("bubble_sort")
# print (bubble_sort(a))
# print ("insertion_sort")
# print (insertion_sort(a))
# print("selection_sort")
# print (selection_sort(a))
print("merge_sort")
print (merge_sort(a))
# BT3051 Pop Quiz 2
# Roll number: BE17B007
# Name: N Sowmya Manojna
# Time: 30

def bubble(l):
	d = len(l)

	if d%2 == 0:
		a = l[:d//2].copy()
		b = l[d//2:].copy()
	else:
		a = l[:d//2 + 1].copy()
		b = l[d//2+1:].copy()
	
	n = len(a)
	m = len(b)

	for i in range(n-1):
		for j in range(n-i-1):
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]

	for i in range(m-1):
		for j in range(m-i-1):
			if b[j]<b[j+1]:
				b[j], b[j+1] = b[j+1], b[j]

	print("Array1:", a)
	print("Array2:", b)

	return [a, b]

inp = list(input().split())

l = []
for i in inp:
	l.append(int(i.strip(',').strip(']').strip('[')))

[a, b] = bubble(l)

# Bubble Sort is stable and O(n*(n-1)/2)
# Stable because equal values aren't swapped

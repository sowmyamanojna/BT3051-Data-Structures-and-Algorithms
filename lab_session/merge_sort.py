def sort(a):
	if len(a)==1:
		return a
	else:
		if len(a)%2 == 0:
			return merge(sort(a[:len(a)//2]), sort(a[len(a)//2:]))
		else:
			return merge(sort(a[:len(a)//2+1]), sort(a[len(a)//2+1:]))

def merge(a, b):
	i = 0
	j = 0

	new_val = []

	while (i < len(a)) and (j < len(b)):
		if a[i] < b[j]:
			new_val.append(a[i])
			i += 1
		elif a[i] > b[j]:
			new_val.append(b[j])
			j += 1
		else:
			new_val.append(a[i])
			new_val.append(b[j])
			i += 1
			j += 1

	if i < len(a):
		new_val.extend(a[i:])
	elif j < len(b):
		new_val.extend(b[j:])

	return new_val

data = input().strip().split()
vals = []
for i in data:
	vals.append(int(i.strip(',').strip('[').strip(']'))) 

print (sort(vals))

# [1, 5, 8, 6564651320, 542384, 62658]
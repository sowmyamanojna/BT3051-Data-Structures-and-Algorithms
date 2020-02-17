[a, b] = map(int, raw_input().split())

if a % 2 == 1:
	a = a
else:
	a += 1

s = 0

for i in range(a,b+1,2):
	s += i

print s
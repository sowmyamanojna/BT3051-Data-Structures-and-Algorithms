from CharStack import CharStack
from ArrayStack import ArrayStack

a = CharStack()
b = CharStack()

c = ArrayStack()
d = ArrayStack()

print(a)
print(b)
a.push('X')
print(a)
print(a._char is b._char)
print(b)
b.push('Y')
print(a)
print(b)

print(c)
print(d)
c.push('X')
print(c)
print(c._data is d._data)
print(d)
d.push('Y')
print(c)
print(d)
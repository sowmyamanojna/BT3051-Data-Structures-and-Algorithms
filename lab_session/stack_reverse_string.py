from character_stack_list import CharStack

A = input("Enter character string: ")
c = CharStack()

for i in A:
	c.push(i)

rev_a = ""

while c.len() != 0:
	rev_a += c.pop()

print("Reversed string:", rev_a)

# # # # import math

# # # # str1 = ('ab', 'cd')
# # # # dict1 = {}
# # # # dict1[str1] = 0
# # # # a = math.pi
# # # # dict1[a] = 0

# # # # print(dict1)

# # # n = 123456789
# # # m = 0
# # # for i in range(len(str(n))):
# # # 	m = 10*m + (n%10)
# # # 	n = n//10

# # # print (m, n)

# # with open('nums.txt') as f:
# # 	x = f.readlines()
# # 	print(x)
# # 	for line in x:
# # 		print(line.strip())
# # 		z = f.readline()
# # 		print (z)

# # print (f.readlines())
# n = int(input())
# for x in range(n):
# 	print (x**x + x^x)

# """
# To demonstrate:

# >>> 0^0
# 0
# >>> 1^1
# 0
# >>> 1^0
# 1
# >>> 0^1
# 1

# To explain one of your own examples:

# >>> 8^3
# 11

# Think about it this way:

# 1000  # 8 (binary)
# 0011  # 3 (binary)
# ----  # APPLY XOR ('vertically')
# 1011  # result = 11 (binary)

# """


class Hello():
	def __init__(self):
		print("Hello ka constructor!")

class World(Hello):
	def __init__(self):
		print("World ka constructor!")

a = World()
from pq1 import BinaryNumber

b1 = BinaryNumber([0, 1, 1, 1])
b2 = BinaryNumber([0, 0, 0, 1])
print (b1)
print (b2)

print (b1.value() + b2.value())

b3 = BinaryNumber([0, 1, 1, 2])

from numericalStack import Stack as ArrayStack
from queueList import Queue as ArrayQueue

stack = ArrayStack()
queue = ArrayQueue()

[stack.push(i) for i in range(1,11)]
[queue.enqueue(i) for i in range(1,11)]

print(stack)
print(queue)

while (not stack.is_Empty()) and stack.top()>=5:
	queue.enqueue(stack.pop())

print()
print(stack)
print(queue)
print()


while (not queue.is_Empty()) and queue.first()<=5:
	stack.push(queue.dequeue())

print(stack)
print(queue)


while not queue.is_Empty():
	print(queue.dequeue())

print('\n')

while not stack.is_Empty():
	print(stack.pop())
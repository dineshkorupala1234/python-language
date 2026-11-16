# STACK
# Stack is a way to organise the items stored in a list
#the last item added is the first one removed.Think of plates arranged  on top of each other: you take the top plate first.
# Stack follows - Last in First Out (LIFO)

stack = ["dinesh","sai","shiva"]
stack.append("deva")
stack.append("naresh")
print(stack)
#here the .append used to add the items
print(stack.pop())   #removes item
print(stack)
print(stack[-2]) #peek
print(stack)

#how it works - if we insert plates one by one .the last plate will be placed on top , and that plate will be taken first ,this is how LIFO works

#QUEUES
# Queue is also a way to organise items in list 
# The queue follow first in first out (FIFO)
#the first item added is the first one removed.people waiting in line: the person who arrived first is served first

queue = ["dinesh","ramesh","suresh"]
queue.append("harish")
queue.append("naresh")
print(queue)
print(queue.pop())
print(queue)
print(queue.pop(0))
print(queue)

#ENQUEUE
# For enqueue we just defaultly use queue to dd items,no need to use enqueue word particularly

#DEQUEUE
#we should start the code by using- from collection import dequeue

from collections import deque
queue = deque(["mahesh","sai","babu"])
print(queue)
queue.append("laxman")
queue.append("venkatesh")
print(queue)
print(queue.pop())
print(queue.pop())
print(queue)
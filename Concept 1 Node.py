# How to create a Node
# A node contain data and details to the next node or link

class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node

    def __str__(self): # This is used to how to display Node object when printed
        return str(self.data)


node1 = Node(10) # Here 10 is the data stored in node and node1 is the object
print(type(node1))

num = 10
print(type(num))

print(num)
print(node1)

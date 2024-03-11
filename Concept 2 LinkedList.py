# https://youtu.be/h29zxRMOXgA?si=99toGU1GRv1WynUN
# Full playlist : https://youtube.com/playlist?list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo&si=lOEvKZgV6K7fnpKA
# For an empty singly linkedlist the head node will be empty that's why we write {self.head = None initially}
# To insert first element to the linkedlist we change head node from None to first Node
# Nodes which are connected linearly are called linkedlist
# If the nodes of linked list contains the data of both next and previous node then it is called doubly linkedlist

# data1,next -> data2,next -> data3,next ->.............

# Steps to create a LinkedList
"""
Step1 : Create nodes
Step2 : Create LinkedList
Step3 : Add nodes to LinkedList
Step4 : Print Linkedlist
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # To insert a new node at the end of a singly linkedlist
    def insertLast(self, newNode):
        # To check the head of the linkedlist is empty then the first node will become the head node
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        # If the list is empty
        if self.head is None:
            print('linkedlist is empty')
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data + '->',end='')
            currentNode = currentNode.next

# This is the first node
# node1.data = 'John' , node1.next = None
node1 = Node('John')
node2 = Node('Ben')
node3 = Node('Mathew')

# Now we can add the above node to the linkedlist, so we want to create a linkedlist object
linkedlist = LinkedList()
linkedlist.insertLast(node1)

# Inserting the second node
linkedlist.insertLast(node2)

# Inserting the third node
linkedlist.insertLast(node3)

# To print the linked list
linkedlist.printList()


"""
https://youtu.be/h29zxRMOXgA?si=99toGU1GRv1WynUN

Through this the above youtube video we have learned,
How to create a node
How to create a linkedlist 
How to insert an element at the end of linked list
How to print a linked list
"""



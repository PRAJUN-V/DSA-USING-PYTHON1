# Python implementation of new node in between two nodes in a linked list
# https://youtu.be/8MCPTf-w3ak?si=CTCzY9zhP27QmqV2

"""
Program logic:
 Step1: Traverse the list till position you want to insert
 Step2: Store the details of previous node
 Step3: Make a connection from the next of previous node to new node
 Step4: Make a connection from the next of new node to remaining node
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
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
        if self.head is None:
            print('Linked list is empty')
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(str(currentNode.data) + '->', end='')
            currentNode = currentNode.next
        print()

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertBetween(self, newNode, position):
        if position < 0 or position > self.listLength():
            print('invalid position')
            return
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


n1 = Node('prajun')
n2 = Node('Ajay')
n3 = Node(5)

l1 = LinkedList()
l1.insertEnd(n1)
l1.insertEnd(n2)

l1.insertBetween(n3, 2)

l1.printList()


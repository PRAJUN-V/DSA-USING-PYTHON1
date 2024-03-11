class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print('Empty linked list')
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.data)
                currentNode = currentNode.next

    def insertBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode

    def searchElement(self, element):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == element:
                return True
            currentNode = currentNode.next
        return False



l1 = LinkedList()
l1.insertBeginning(12)
l1.insertBeginning(13)
l1.insertBeginning(14)
l1.insertEnd(15)

l1.printLL()
print(l1.searchElement(16))

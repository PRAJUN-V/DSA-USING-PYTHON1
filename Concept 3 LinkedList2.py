# https://youtu.be/nH_nhfEZ7hc?si=YlXDRW6bNCq3c18Y
# Python implementation of the head node insertion in singly linked list

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

    def insertHead(self, newNode):    # This is how we insert a element at head in linked list
        tempNode = self.head          # First store head node in a temporary node otherwise the connection will be lost
        self.head = newNode           # Then point head to the newNode
        self.head.next = tempNode     # Then connect previous headNode to the next of new headNode
        del tempNode                  # Finally delete the temporaryNode which is not needed anymore


n1 = Node('prajun')
n2 = Node('Ajay')
n3 = Node(5)

l1 = LinkedList()

l1.insertEnd(n1)
l1.insertEnd(n2)

l1.insertHead(n3)

l1.printList()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode

        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode

    def deleteFirstNode(self):
        self.head = self.head.next







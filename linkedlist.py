class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.size = 0
        self.tail = self.head
    
    def insertAtEnd(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1
    
    def insertAtHead(self, data):
        remainingListHead = self.head.next
        self.head.next = Node(data)
        self.head.next.next = remainingListHead
        self.size += 1

    def insertAtPos(self, pos, data):
        if self.size < pos:
            return

        currPos = 1
        currPtr = self.head

        while currPos < pos:
            currPtr = currPtr.next
            currPos += 1
        
        restOfListHead = currPtr.next
        currPtr.next = Node(data)
        currPtr.next.next = restOfListHead

    def deleteAll(self):
        self.head.next = None

    def deleteStartingFromPos(self,pos):
        currPos = 1
        currPtr = self.head

        while currPos < pos:
            currPtr = currPtr.next
            currPos += 1
        
        currPtr.next = None

        numDeleted = self.size - pos + 1
        self.size -= numDeleted

    def deleteAtPos(self, pos):
        if self.size < pos:
            return

        currPos = 1
        currPtr = self.head

        while currPos < pos:
            currPtr = currPtr.next
            currPos += 1
        
        currPtr.next = currPtr.next.next
        self.size -= 1


    def __repr__(self):
        currPtr = self.head.next
        repr = ""
        while currPtr:
            repr += str(currPtr.data) + " , "
            currPtr = currPtr.next
        return repr[:-2]
    
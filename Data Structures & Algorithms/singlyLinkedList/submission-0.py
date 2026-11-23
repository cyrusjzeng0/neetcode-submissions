class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index >= self.size: 
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            second = self.head # current head will be second in list after insertion
            self.head = Node(val, second)
        
        self.size += 1


    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        if index == 0: # remove head
            self.head = self.head.next # shift head to second position
        else:
            curr = self.head
            for i in range(index-1): # traverse to node before index
                curr = curr.next
            curr.next = curr.next.next # set next of node before index to the node after
            if index == self.size - 1:
                self.tail = curr # set self.tail to node before index
        


        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        curr = self.head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

# Name: Jay Razdan

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
        # (a) Initialize the linked list with an additional tail pointer:
        self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item, self.head)
        self.head = temp
    
    # (b) Implementing the remove() function:
    def remove(self):
        new = self.head.next # define the eventual new head/front of the list as the next node from the current head/front
        self.head = None # erase the current head
        self.head = new # define the head/front of the list now as previously defined "new" head/front
    # Since this method takes the same amount of time, regardless of list length, the time complexity is: Θ(1)

    # (c) Implementing the removeAtEnd() function:
    def removeAtEnd(self):
        n = self.head # establish a pointer n at the start of the list
        # if n points to an empty head or if n points to a head whose next node is empty, we are removing nothing or the last element of the list, respectively; 
        # so, clear the head element, if any
        if n == None or n.next == None: 
            self.head = None
        # otherwise, we iterate the pointer n until its next node is the last element in the list;
        # erase the last element, and then set the tail equal to the node at n
        else:
            while n.next.next is not None:
                n = n.next
            n.next = None
            self.tail = n
        # For a list length n, greater than or equal to 2, we must iterate n-1 times;
        # so, the time complexity is: Θ(n)

# Name: Jay Razdan

# (a) Define a Node class with a "prev" attribute, and incorporate this into the Sdll class
class Node:
    def __init__(self, item, prev, next):
        self.item = int(item)
        self.prev = prev
        self.next = next 

class Sdll:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item, None, self.head)
        self.head = temp
    
# (b) There are 4 cases of insertion:
    def insert(self, x):
        # Case 1 and 2: the item we will insert will be the first and smallest, respectively 
        if self.isEmpty() or x < self.head.item:
            temp = Node(x, None, self.head)
            self.head = temp
            self.tail = temp
        else:
            c = self.head
            temp = Node(x, None, self.head)
            count = 1
            # Case 2: the item we will insert will be somewhere in the middle
            while c.next is not None and count == 1:
                if temp.item >= c.item and temp.item <= c.next.item:
                    temp = Node(x, c, c.next)
                    c.next.prev = temp
                    c.next = temp
                    count -= 1
                else:
                    c = c.next
            # Case 3: the item we will insert will be the largest
            if c.next is None:
                temp = Node(x, c, None)
                c.next = temp
                self.tail = temp

# (c)
    def delete(self, x):
        current = self.head
        # loop through the list until we find a value greater than x
        while current is not None:
            # if we find a node with item equal to x, we remove it
            if current.item == x:
                # if current is the head node, we must update the head;
                # similarly, if current is the tail, we must update the tail;
                # for that matter, we must update the next and previous attributes of the next and previous nodes to the one we deleted, if it was in the middle
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                # once we have deleted a node, we move to the next one by updating current
                next_node = current.next
                current = next_node
            # because the list is sorted, once the item attribute of current is greater than x, we stop;
            # otherwise, we update current
            elif current.item > x:
                break
            else:
                current = current.next 

# (d)
    # we employ the add method from earlier to add the items 
    def reverseString(self):
        # define a new empty linked list and loop through the original linked list from head to tail;
        # each time, adding the next node to the new linked list;
        # this will construct a linked list that is the reverse of the original
        reverse = Sdll()
        r = self.head
        while r is not None:
            reverse.add(r.item)
            r = r.next
        return reverse

    # we define a printing procedure with conditionals to print for every case of Sdll
    def __str__(self):
        current = self.head
        result = ""
        # if linked list is empty, print "None"
        if self.isEmpty():
            result += "None"
            return result
        # given there is a first node:
        if current.prev is None and current is not None:
            result += "None <- "
        # then we can loop through the linked list with the "current" pointer;
        # if current is in the middle, then we have "<->" after its item;
        # otherwise, it must be the last node, so we have "-> None" after its item, and we end the loop
        while current is not None:
            if current.next is not None:
                result += f"{current.item} <-> "
                current = current.next
            else:
                result += f"{current.item} -> None"
                break
        return result

# Example usage:
mysortedlist = Sdll()
mysortedlist.insert(3)
mysortedlist.insert(1)
mysortedlist.insert(6)
mysortedlist.insert(3)
mysortedlist.insert(1)
mysortedlist.insert(3)
print(mysortedlist)
print(mysortedlist.reverseString())
mysortedlist.delete(3)
print(mysortedlist)
print(mysortedlist.reverseString())

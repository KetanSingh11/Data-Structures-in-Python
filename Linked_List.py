#===================================================
""" Linked List Implementation in PYTHON """
#===================================================


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data    # contains the data
        self.next = next    # contains the reference
        
    def __str__(self):
        return str(self.data)   # prints the data
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def insert_first(self, data):
        '''inserts the new Node at the start of the list'''
        new_node = Node(data, self.head)
        self.head = new_node    #here, making new node as new head
        self.size += 1

    def delete(self, data):
        '''
        # Start from the Root node
        # Check if root matches the data;
                then shift the root to the root.next
                else mode to the next node
        # else move to the next node;
                if match found, point the prev node to the node next to current
        '''
        current = self.head     #start for the root/head
        prev_node = None
        
        while current:
            if current.data == data:
                if prev_node:       #means current is NOT a root node 
                    prev_node.next = current.next
                else:
                    #current is the root node
                    self.head = current.next
                
                self.size -=1
                return True         #node found
            else:
                prev_node = current
                current = current.next
                
        
        #if node is not found inside while loop
        return False       
    
    def printList(self):
        current = self.head
        while current:
            print(str(current.data) + "-->",end="")
            current = current.next
        print("NULL")
    
    def get_size(self):    
        print("LinkedList size: " + str(self.size))


if __name__ == "__main__":
    a = LinkedList()
    a.insert_first(10)
    a.insert_first(20)
    a.insert_first(30)
    a.printList()
    a.get_size()
    
    a.delete(10)
    a.printList()
    print(a.isEmpty())
    
    a.delete(20)
    a.printList()
    a.delete(30)
    a.printList()
    print(a.isEmpty())
    
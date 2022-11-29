class Node:
    #constructor
    def __init__ (self):
        self.data =None
        self.next =None
    #method for setting the data field of the node
    def setData(self,data):
        self.data =data
    #method for getting the data field of the node
    def getData(self):
        return seld.data
    #method for setting the next field of the node
    def setNext(self,next):
        self.next = next
    #method for getting the next field of the node
    def getNext(self):
        return self.next
    #returns true if the node points to another node
    def hasNext(self):
        return self.next !=None

#Transversing the linked list
def listLength(self):
    current = self.head
    count =0

    while current !=None :
        count = count +1 
        current = current.getNext()
    return count

#insertinfg in Linked List 
#before the head node
def insertAtBeginning(self,data):
    newNode = Node()
    newNode.setData(Data)

    if self.length == 0:
        self.head =newNode
    else:
        newNode.setNext(self.head)
        self.head =newNode

    self.length +=1



#inserting at the end of a linked list
def insertAtEnd(self,data):
    newNode =Node()
    newNode.setData(Data)
    
    current = self.head
    while current.getNext() !=None:
        current = current.getNext()

    current.setNext(newNode)
    self.length +=1

#inserting at the middle of two nodes 
#method for inserting a new node at any position in a linked list
def insertAtPos(self,pos,data):
    if pos> self.length or pos<0:
        return None
    else:
        if pos==0:
            self.insertAtBeg(data)
        else:
            if pos ==self.length:
                self.insertAtEnd(data)
            else:
                newNode = Node()
                newNode.setData(data)
                count = 0
                current = self.head
                while count<pos-1:
                    count +=1
                    current = current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self.lenght +=1
                



import time
start_time=time.time()
class Node(object):

	def _init_(self, data):
		self.data = data
		self.nextNode = None
		
class LinkedList(object):
    def _init_(self):
        self.head = None
        self.size = 0
		
    def insertEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode


    def duplicate(self):
        dictionary={}
        newnode=None
        start=None
        currentNode=self.head
        while currentNode is not None:
            if currentNode.data not in dictionary:
                dictionary[currentNode.data]=currentNode.data
                if newnode is None:
                    newnode=currentNode
                    start=newnode
                else:
                    newnode.nextNode=currentNode
                    newnode=currentNode

            currentNode=currentNode.nextNode
        newnode.nextNode=None

                
    
        while start is not None:
            print("%d " % start.data,end=" ")
            start = start.nextNode



linkedlist=LinkedList()

linkedlist.insertEnd(1)
linkedlist.insertEnd(2)
linkedlist.insertEnd(3)
linkedlist.insertEnd(2)
linkedlist.insertEnd(2)
linkedlist.insertEnd(112)
linkedlist.insertEnd(1)

linkedlist.duplicate()

print()
print(time.time()-start_time)
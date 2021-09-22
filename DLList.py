from DLNode import DLNode

class DLList:
    def __init__(self,head=None):
        self.head=head
    def add_to_front(self, val):
        new_node = DLNode(val,next=self.head)
        self.head=new_node
        return self
    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = DLNode(val)
        runner = self.head
        while runner.next!= None:
            runner = runner.next
        runner.next = new_node
        new_node.prev=runner
        return self
    def print_values(self):
        runner = self.head
        while runner!=None:
            print (runner.value)
            runner = runner.next
        return self
    def delNode(self,val=None,index=None):
        runner = self.head
        prev_node = None
        counter = 0
        while runner!=None:
            if runner.value == val or counter==index:
                if prev_node != None:
                    runner.next.prev = prev_node
                    prev_node.next = runner.next
                    del runner
                    break
                else:
                    runner.next.prev = None
                    self.head = runner.next
                    del runner
                    break
            prev_node = runner
            runner= runner.next
            counter +=1
        return self
    def insertNode(self,val,index=None, val_neigh = None):
        if self.head == None:
            self.add_to_front(val)
            return self
        newNode = DLNode(val)
        runner = self.head
        prev_node = None
        counter = 0
        while runner!=None:
            if runner.value == val_neigh or counter==index-1:
                if prev_node != None:
                    newNode.prev = runner
                    newNode.next = runner.next
                    runner.next = newNode
                    break
                elif prev_node== None:
                    self.add_to_back(val)
                    break
            prev_node = runner
            runner= runner.next
            counter +=1
        return self

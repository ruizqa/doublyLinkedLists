from DLNode import DLNode
from DLList import DLList

List1 = DLList()
List1.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!

testList = DLList()

testList.insertNode("first",index = 0).insertNode("second",index =1).insertNode("second",index =1).insertNode("last",index=3).print_values()
testList.delNode(val="second").print_values()

from linkList import *

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.print_list()

llist.rotate(4)
print("After Rotation around element 4")
llist.print_list()


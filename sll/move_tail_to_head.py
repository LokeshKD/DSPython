from linkList import *

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Before moving tail to head")
llist.print_list()
llist.move_tail_to_head()
print("After moving tail to head")
llist.print_list()

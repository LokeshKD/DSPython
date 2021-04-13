from linkList import *

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.reverse_recursive()

print("Recursive Reverse")
llist.print_list()

llist.reverse_iterative()

print("Iterative Reverse")
llist.print_list()

from circularLL import *

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
print("List is...")
cllist.print_list()

cllist.remove("A")
cllist.remove("C")
print("List after removal is...")
cllist.print_list()

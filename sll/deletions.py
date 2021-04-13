from linkList import *

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Deletions by value")
llist.delete_node("B")
llist.delete_node("E")

llist.print_list()

print("Deletions by Position")
llist.delete_node_at_pos(0)

llist.print_list()

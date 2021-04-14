from doubleLL import *

dllist = DoublyLinkedList()
dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)
dllist.print_list()

print("After Dups removal")
dllist.remove_duplicates()
dllist.print_list()

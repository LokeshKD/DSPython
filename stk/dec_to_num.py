from stack import Stack

def convert_int_to_bin(dec_num):
  rem = Stack()
  bin_num = ""
  
  while dec_num > 0:
    rem.push(dec_num % 2)
    dec_num //= 2

  while not rem.is_empty():
    bin_num += str(rem.pop())

  return bin_num


print(convert_int_to_bin(4))

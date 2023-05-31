command_list = ['ADD', 'SUB', 'MOV', 'AND', 'OR', 'NOT', 'MULT', 'LSFTL', 'LSFTR', 'ASFTR', 'RL', 'RR']

n = int(input())
orders = []

def convert_to_binary(num, length):
  return str(bin(int(num))[2:]).zfill(length)

for _ in range(n):
  orders.append(list(input().split()))

for opcode, r1, r2, r3 in orders:
  is_inclue_c = False
  if opcode not in command_list:
    is_inclue_c = True
    opcode = opcode[:-1]
  
  command = convert_to_binary(command_list.index(opcode), 4)
  command += '1' if is_inclue_c else '0'
  command += '0'
  command += convert_to_binary(r1, 3)
  command += convert_to_binary(r2, 3)
  
  if is_inclue_c:
    command += convert_to_binary(r3, 4)
  else:
    command += convert_to_binary(r3, 3)
    command += '0'

  print(command)
  
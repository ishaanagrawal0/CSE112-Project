'''
Aditya Gupta 2022031
Debjit Banerji 2022146
Himang Chandra Garg 2022214
Ishaan Agrawal 2022221
'''

registers={
    "000": "R0",
    "001": "R1",
    "010": "R2",
    "011": "R3",
    "100": "R4",
    "101": "R5",
    "110": "R6",
    "111": "FLAGS"
}

register_values = {
    "R0": 0,
    "R1": 0,
    "R2": 0,
    "R3": 0,
    "R4": 0,
    "R5": 0,
    "R6": 0,
    "FLAGS": 0
}

zero = 0000000000000000
register_output = [zero,zero,zero,zero,zero,zero,zero,zero]

f1 = open("stdout.txt", "r")
MEM = f1.readlines()
for i in range(len(MEM)):
    MEM[i] = MEM[i].strip()
f1.close()
print(MEM)


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def decimalToBinary(decimal):
    decimal1 = decimal
    binary, i, n = 0, 0, 0
    while(decimal != 0):
        binary = binary + (decimal % 2) * pow(10, i)
        decimal = decimal//2
        i += 1
    return binary

#Type-A Binary encodings

def add(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:16]]
    if decimalToBinary(binaryToDecimal(register_values[regB]) + binaryToDecimal(register_values[regC]))<=1111111:
        register_values[regA] = decimalToBinary(binaryToDecimal(register_values[regB]) + binaryToDecimal(register_values[regC]))
    else:
        #Write the FLAGS condition for overflow here.
        register_values[regA] = 0000000

def sub(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:16]]
    if (register_values[regB]) < binaryToDecimal(register_values[regC]):
        register_values[regA] = 0000000
        #Write the FLAGS condition for overflow here.
    else:
        register_values[regA] = decimalToBinary(binaryToDecimal(register_values[regB]) - binaryToDecimal(register_values[regC]))

for i in MEM:
    if i == '1101000000000000':
        exit() #GC se exit
    else:
        pass
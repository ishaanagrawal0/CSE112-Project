'''
Aditya Gupta 2022031
Debjit Banerji 2022146
Himang Chandra Garg 2022214
Ishaan Agrawal 2022221
'''

MAX_INT=(2**16-1)
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
dictionary_of_reg_binary={"R0":'0000000000000000',
                          "R1":'0000000000000000',
                          'R2':'0000000000000000',
                          "R3":'0000000000000000',
                          "R4":'0000000000000000',
                          "R5":'0000000000000000',
                          "R6":'0000000000000000',
                          "FLAGS":'0000000000000000'}
#All registers in this dictionary are storing integers except for the flags register which is storing a string indicating the binary value
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

initial_value = '0000000000000000'
register_output = [initial_value,initial_value,initial_value,initial_value,initial_value,initial_value,initial_value,initial_value]

f1 = open(r"C:\Users\adity\Downloads\stdout.txt", "r")
MEM = f1.readlines()
for i in range(len(MEM)):
    MEM[i] = MEM[i].strip()  # for the extra spaces(if any in the binary code)
f1.close()
#print(MEM)


def binaryToDecimal(binary):
    binary1 = str(binary)
    decimal, i, n = 0, 0, 0
    for i in range(len(binary1)):
        if(binary1[i] == '1'):
            decimal += 2**i

    return decimal

# def decimalToBinary(decimal):
#    decimal1 = decimal
#    binary, i, n = 0, 0, 0
#    while(decimal != 0):
#        binary = binary + (decimal % 2) * pow(10, i)
#        decimal = decimal//2
#        i += 1
#    return binary

#Type-A Binary encodings

def add(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    regF = registers['111']
    
    if register_values[regB] + register_values[regC] <= MAX_INT:
        register_values[regA] = register_values[regB] + register_values[regC]
        dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
        
        
    else:
        #Write the FLAGS condition for overflow here.
        dictionary_of_reg_binary[regF] = dictionary_of_reg_binary[regF][:12]+'1'+dictionary_of_reg_binary[regF][13:]
        register_values[regA] = 0
        dictionary_of_reg_binary[regA]='0'*16

def sub(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    regF = registers['111']
    if (register_values[regB]) < register_values[regC]:
        register_values[regA] = 0
        dictionary_of_reg_binary[regA]='0'*16
        register_values[regF] = register_values[regF][:12]+'1'+register_values[regF][13:]
    else:
        register_values[regA] =(register_values[regB])-(register_values[regC])
        dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
        

def mul(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    regF = registers['111']
    if (register_values[regB]) * (register_values[regC]) <= MAX_INT:
        register_values[regA] = (register_values[regB]) * (register_values[regC])
        dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
    else:
        #Write the FLAGS condition for overflow here.
        register_values[regF] = register_values[regF][:12]+'1'+register_values[regF][13:]
        register_values[regA] = 0
        dictionary_of_reg_binary[regA]='0'*16
        

def xor(i):
    regA = registers[i[7:10]]   
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    register_values[regA] =register_values[regB]^(register_values[regC])
    dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]

def OR(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    register_values[regA] =(register_values[regB]) | (register_values[regC])
    dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]


def AND(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    register_values[regA] =(register_values[regB]) & (register_values[regC])
    dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
    
#Type-B Binary encodings

def mov_imm(i):
    regA = registers[i[6:9]]
    imm = i[9:]
    # register_values[regA] = int(imm)
    register_values[regA] = binaryToDecimal(imm)
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]
    
def left_shift(i):
    regA = registers[i[6:9]]
    imm = i[9:15]
    register_values[regA] = binaryToDecimal(imm) << 1
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]

def right_shift(i):
    regA = registers[i[6:9]]
    imm = i[13:16]
    register_values[regA] = binaryToDecimal(imm) >> 1
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]

#Type-C Binary encodings

def mov_reg(i):
    regA = registers[i[10:13]]
    regB = registers[i[13:16]]
    register_values[regA] = register_values[regB]
    dictionary_of_reg_binary[regA] = dictionary_of_reg_binary[regB]
    
def Invert(i):
    regA = registers[i[10:13]]
    regB = registers[i[13:16]]
    register_values[regA] = ~ binaryToDecimal(register_values[regB]) # binaryToDecimal((2**16)-binaryToDecimal(register_values[regB])-1)
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]

def Divide(i):
    regA = registers[i[10:13]]
    regB = registers[i[13:]]
    regF = registers["111"]
    if(register_values[regB] == 0):
        register_values[regF] = register_values[regF][:12]+'1'+register_values[regF][13:]
        register_values['000'] = 0
        dictionary_of_reg_binary['000'] = '0'*16
        register_values['001'] = 0
        dictionary_of_reg_binary[registers['001']] = '0'*16
    else:
        register_values['000'] = register_values[regA]//register_values[regB]
        dictionary_of_reg_binary[registers['000']] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]
        register_values['001'] = register_values[regA]%register_values[regB]
        dictionary_of_reg_binary[registers['000']] = (16-len(bin(register_values[regB])[2:]))*'0' + bin(register_values[regB])[2:]

def cmp(i):
    regA = registers[i[10:13]]
    regB = registers[i[13:]]
    regF = registers["111"]
    if register_values[regA] > register_values[regB]:
        register_values[regF] = '0000000000000010'
    elif register_values[regA] < register_values[regB]:
        register_values[regF] = '0000000000000100'
    else:
        register_values[regF] = '0000000000000001'

#Type-D Binary encodings

def ld(i):
    regA = registers[i[6:9]]
    regAddr = registers[i[9:]]
    a = binaryToDecimal(regAddr)
    dictionary_of_reg_values[regA] = MEM[a]
    register_values[regA] = binaryToDecimal(dictionary_of_reg_values[regA])
4
def st(i):
    regA = registers[i[6:9]]
    regAddr = registers[i[9:]]
    a = binaryToDecimal(regAddr)
    dictionary_of_reg_values[regA] = MEM[a]
    register_values[regA] = binaryToDecimal(dictionary_of_reg_values[regA])

#Type-E Binary encodings
def jmp(i):
    PC = binaryToDecimal(i[9:])
    return PC
    
def jlt(i):
    if(dictionary_of_reg_binary['111'][13] =='1'):
        PC = binaryToDecimal(i[9:])
        return PC
    else:
        return 0

def jgt(i):
    if (dictionary_of_reg_binary['FLAGS'][14] =='1'):
        PC = binaryToDecimal(i[9:])
        return PC
    else:
        return 0

def je(i):
    if(dictionary_of_reg_binary['FLAGS'][15] == '1'):
        PC = binaryToDecimal(i[9:])
        return PC
    else:
        return 0

#Type-F Binary encodings

def halt(i):
    exit()
    
# Floating Point Arithmetic Operations    
#def addf(i):
    
    
#def subf(i):
    
    
#def movf(i):
    
    
PC = 0 # Program Counter
f1 = 0 # Flag for PC to be incremented or not

while(True):
    f1 = 0
    if MEM[PC][:5] == '11010':
        #this is halt command
        for h in MEM:
            print(h) #printin the memory at the end
        break #GC se exit
    else:
        opcode = MEM[PC][0:5]
        if opcode == "00000":
            add(MEM[PC])
        elif opcode == "00001":
            sub(MEM[PC])
        elif opcode == "00110":
            mul(MEM[PC])
        elif opcode == "01010":
            xor(MEM[PC])
        elif opcode == "01011":
            OR(MEM[PC])
        elif opcode == "01100":
            AND(MEM[PC])
        elif opcode == "00010":
            mov_imm(MEM[PC])
        elif opcode == "01000":
            right_shift(MEM[PC])
        elif opcode == "01001":
            left_shift(MEM[PC])
        elif opcode == "00011":
            mov_reg(MEM[PC])
        elif opcode == "01101":
            Invert(MEM[PC])
        elif opcode == "00111":
            Divide(MEM[PC])  # Handle other opcodes here
        elif opcode == '01110':
            cmp(MEM[PC])
        elif opcode == '00100':
            ld(MEM[PC])
        elif opcode == '00101':
            st(MEM[PC])
        elif opcode == '01111':
            a = jmp(MEM[PC])
            f1 = 1
        elif opcode == '11100':
            a = jlt(MEM[PC])
            if(a != 0):
                PC = a
                f1 = 1 
        elif opcode == '11101':
            a = jgt(MEM[PC])
            if(a != 0):
                PC = a
                f1 = 1
        elif opcode == '11111':
            a = je(MEM[PC])
            if(a != 0):
                PC = a
                f1 = 1
            
    a = bin(PC)
    a1 = ('0'*(7-len(a[2:]))) + str(a[2:])
    if(f1==0):
        PC += 1
    #a2 = [('0'*(16-len(bin(register_values[i])[2:])))+bin(register_values[i])[2:] for i in register_values.keys()]
    #a1.extend(a2)
    print(a1+" "+dictionary_of_reg_binary["R0"]+" "+dictionary_of_reg_binary["R1"]+" "+dictionary_of_reg_binary["R2"]+" "+dictionary_of_reg_binary["R3"]+" "+dictionary_of_reg_binary["R4"]+" "+dictionary_of_reg_binary["R5"]+" "+dictionary_of_reg_binary["R6"]+" "+dictionary_of_reg_binary["FLAGS"]+" ")

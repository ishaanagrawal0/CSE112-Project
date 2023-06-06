'''
Aditya Gupta 2022031
Debjit Banerji 2022146
Himang Chandra Garg 2022214
Ishaan Agrawal 2022221
'''
import sys
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
dictionary_of_variables={} #this stores the variable : its address

dictionary_of_label_addresses_decimal={} #this stores the variable : its value


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
variable_number_counter=1

initial_value = '0000000000000000'
register_output = [initial_value,initial_value,initial_value,initial_value,initial_value,initial_value,initial_value,initial_value]

#f1 = open(r"C:\Users\adity\Downloads\stdout.txt", "r")
#MEM = f1.readlines()
MEM=sys.stdin.readlines()
for i in range(len(MEM)):
    MEM[i] = MEM[i].strip()  # for the extra spaces(if any in the binary code)
#f1.close()
#print(MEM)


def binaryToDecimal(binary):
    binary1 = str(binary)[::-1]
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
        dictionary_of_reg_binary["FLAGS"]='0'*16
        register_values["FLAGS"]=0
        
    else:
        #Write the FLAGS condition for overflow here.
        dictionary_of_reg_binary[regF] = '0000000000001000'
        register_values[regF]=binaryToDecimal(dictionary_of_reg_binary[regF])
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
        dictionary_of_reg_binary[regF] = '0000000000001000'
        register_values[regF]=binaryToDecimal(dictionary_of_reg_binary[regF])
    else:
        register_values[regA] =(register_values[regB])-(register_values[regC])
        dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
        dictionary_of_reg_binary["FLAGS"]='0'*16
        register_values["FLAGS"]=0

def mul(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    regF = registers['111']
    if (register_values[regB]) * (register_values[regC]) <= MAX_INT:
        register_values[regA] = (register_values[regB]) * (register_values[regC])
        dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
        dictionary_of_reg_binary["FLAGS"]='0'*16
        register_values["FLAGS"]=0
    else:
        #Write the FLAGS condition for overflow here.
        dictionary_of_reg_binary[regF] = '0000000000001000'
        register_values[regF]=binaryToDecimal(dictionary_of_reg_binary[regF])
        register_values[regA] = 0
        dictionary_of_reg_binary[regA]='0'*16
        

def xor(i):
    regA = registers[i[7:10]]   
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    register_values[regA] =register_values[regB]^(register_values[regC])
    dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
def OR(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    register_values[regA] =(register_values[regB]) | (register_values[regC])
    dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0

def AND(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    register_values[regA] =(register_values[regB]) & (register_values[regC])
    dictionary_of_reg_binary[regA]=(16-len(str(bin(register_values[regA]))[2:]))*'0'+str(bin(register_values[regA]))[2:]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
#Type-B Binary encodings

def mov_imm(i):
    regA = registers[i[6:9]]
    imm = i[9:]
    # register_values[regA] = int(imm)
    register_values[regA] = binaryToDecimal(imm)
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
def left_shift(i):
    regA = registers[i[6:9]]
    imm = i[9:15]
    register_values[regA] = binaryToDecimal(imm) << 1
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
def right_shift(i):
    regA = registers[i[6:9]]
    imm = i[13:16]
    register_values[regA] = binaryToDecimal(imm) >> 1
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
#Type-C Binary encodings

def mov_reg(i):
    regA = registers[i[10:13]]
    regB = registers[i[13:16]]
    #register_values[regA] = register_values[regB]
    dictionary_of_reg_binary[regA] = dictionary_of_reg_binary[regB]
    register_values[regA] = binaryToDecimal(dictionary_of_reg_binary[regA])
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
def Invert(i): 
    regA = registers[i[10:13]]
    regB = registers[i[13:16]]
    register_values[regA] = ~ binaryToDecimal(register_values[regB]) # binaryToDecimal((2**16)-binaryToDecimal(register_values[regB])-1)
    dictionary_of_reg_binary[regA] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
def Divide(i):
    regA = registers[i[10:13]]
    regB = registers[i[13:]]
    regF = registers["111"]
    if(register_values[regB] == 0):
        dictionary_of_reg_binary[regF] = '0000000000001000'
        register_values[regF]=binaryToDecimal(dictionary_of_reg_binary[regF])
        register_values['000'] = 0
        dictionary_of_reg_binary['000'] = '0'*16
        register_values['001'] = 0
        dictionary_of_reg_binary[registers['001']] = '0'*16
    else:
        register_values['000'] = register_values[regA]//register_values[regB]
        dictionary_of_reg_binary[registers['000']] = (16-len(bin(register_values[regA])[2:]))*'0' + bin(register_values[regA])[2:]
        register_values['001'] = register_values[regA]%register_values[regB]
        dictionary_of_reg_binary[registers['000']] = (16-len(bin(register_values[regB])[2:]))*'0' + bin(register_values[regB])[2:]
        dictionary_of_reg_binary["FLAGS"]='0'*16
        register_values["FLAGS"]=0
def cmp1(i):
    regA = registers[i[10:13]]
    regB = registers[i[13:]]
    regF = registers["111"]
    if register_values[regA] > register_values[regB]:
        dictionary_of_reg_binary[regF] = '0000000000000010'
    elif register_values[regA] < register_values[regB]:
        dictionary_of_reg_binary[regF] = '0000000000000100'
    else:
        dictionary_of_reg_binary[regF] = '0000000000000001'

#Type-D Binary encodings

def ld(i,variable_number_counter):
    regA = registers[i[6:9]]
    dictionary_of_variables[f"var{variable_number_counter}"]=i[9:]
    dictionary_of_label_addresses_decimal[f'var{variable_number_counter}']=0

    register_values[regA] = dictionary_of_label_addresses_decimal[f'var{variable_number_counter}']
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
def st(i,variable_number_counter):
    regA = registers[i[6:9]]
    dictionary_of_variables[f'var{variable_number_counter}']=i[9:]
    dictionary_of_label_addresses_decimal[f'var{variable_number_counter}']=register_values[regA]
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0

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
# Assuming the exponent bits go from -3 to +4
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num
def float_bin(number, places = 3):
    if (float(number)==0):
        return '00000'
    # split() separates whole number and decimal
    # part and stores it in two separate variables
    whole, dec = str(number).split(".")
 
    # Convert both whole number and decimal 
    # part from string type to integer type
    whole = int(whole)
    dec = int (dec)
 
    res = bin(whole).lstrip("0b") + "."
 

    for x in range(places):
        
        try:
            whole, dec = str((decimal_converter(dec)) * 2).split(".")
        except:
            ValueError
            break
 
        dec = int(dec)

        res += whole
    res=str(res).replace(".","")
    res=res+(5-len(res))*'0'
    return res

def floating_conversion_from_bit(bits):
    exponent=binaryToDecimal(bits[:3])
    i= (-1)
    mantissa_decimal=0
    for g in bits[3:]:
        if g=='1':
            mantissa_decimal+=2**(i)
        i-=1
    ans=(1+mantissa_decimal)*(2)**(exponent-3) # 3 is the bias
    
    return ans
        
    
def addf(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    regF = registers['111']
    if  register_values[regB] + register_values[regC] < 31.5:
        register_values[regA] = register_values[regB] + register_values[regC]
        if register_values[regA]>1:
            exponent_part=0
        else:
            exponent_part= (-3)
        while(register_values[regA]//(2**(exponent_part))!=1):
            exponent_part+=1
        #print(exponent_part)

        number_left=(register_values[regA]/2**(exponent_part))-1
        #print(float_bin(number_left,5))
        mantissa=float_bin(number_left,5)
        exponent_part+=3
        dictionary_of_reg_binary[regA]=8*'0'+(3-len(bin(exponent_part)[2:]))*'0'+bin(exponent_part)[2:]+mantissa
        dictionary_of_reg_binary["FLAGS"]='0'*16
        register_values["FLAGS"]=0
    else:
        dictionary_of_reg_binary[regF] = '0000000000001000'
        register_values[regF]=binaryToDecimal(dictionary_of_reg_binary[regF])
        register_values[regA] = 0
        dictionary_of_reg_binary[regA]='0'*16

def subf(i):
    regA = registers[i[7:10]]
    regB = registers[i[10:13]]
    regC = registers[i[13:]]
    regF = registers['111']
    if register_values[regB] - register_values[regC] > 0.125: # for the overflow in the floating point case we have considered for the 0.125 case which is (1.00000 * 2^(-3))
        register_values[regA]=register_values[regB]-register_values[regC]
        if register_values[regA]>1:
            exponent_part=0
        else:
            exponent_part= (-3)
        while(register_values[regA]//(2**(exponent_part))!=1):
            exponent_part+=1
        #print(exponent_part)

        number_left=(register_values[regA]/2**(exponent_part))-1
        #print(float_bin(number_left,5))
        mantissa=float_bin(number_left,5)
        exponent_part+=3
        dictionary_of_reg_binary[regA]=8*'0'+(3-len(bin(exponent_part)[2:]))*'0'+bin(exponent_part)[2:]+mantissa
        dictionary_of_reg_binary["FLAGS"]='0'*16
        register_values["FLAGS"]=0
    else:
        dictionary_of_reg_binary[regF] = '0000000000001000'
        register_values[regF]=binaryToDecimal(dictionary_of_reg_binary[regF])
        register_values[regA] = 0
        dictionary_of_reg_binary[regA]='0'*16
        

def movf(i):
    regA=registers[i[5:8]]
    decimal_value=floating_conversion_from_bit(i[8:])
    register_values[regA]=decimal_value
    
    dictionary_of_reg_binary[regA]=8*'0'+i[8:]    
    dictionary_of_reg_binary["FLAGS"]='0'*16
    register_values["FLAGS"]=0
    
    
        
    
        
        

    
    
    
    
PC = 0 # Program Counter
PC_PRINTED=0
f1 = 0 # Flag for PC to be incremented or not

while(True):
    f1 = 0
    if MEM[PC][:5] == '11010':
        #this is halt command
        dictionary_of_reg_binary['FLAGS']=16*'0'
        register_values['FLAGS']=0
        a = bin(PC)
        a1 = ('0'*(7-len(a[2:]))) + str(a[2:])
        print(a1+"        "+dictionary_of_reg_binary["R0"]+" "+dictionary_of_reg_binary["R1"]+" "+dictionary_of_reg_binary["R2"]+" "+dictionary_of_reg_binary["R3"]+" "+dictionary_of_reg_binary["R4"]+" "+dictionary_of_reg_binary["R5"]+" "+dictionary_of_reg_binary["R6"]+" "+dictionary_of_reg_binary["FLAGS"]+" ")
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
            cmp1(MEM[PC])
        elif opcode == '00100':
            ld(MEM[PC],variable_number_counter)
            variable_number_counter+=1
        elif opcode == '00101':
            st(MEM[PC],variable_number_counter)
            variable_number_counter+=1
        elif opcode == '01111':
            a = jmp(MEM[PC])
            PC=a
            dictionary_of_reg_binary["FLAGS"]='0'*16
            f1 = 1
        elif opcode == '11100':
            a = jlt(MEM[PC])
            if(a != 0):
                PC = a
                f1 = 1 
            dictionary_of_reg_binary["FLAGS"]='0'*16
        elif opcode == '11101':
            a = jgt(MEM[PC])
            if(a != 0):
                PC = a
                f1 = 1
            dictionary_of_reg_binary["FLAGS"]='0'*16
        elif opcode == '11111':
            a = je(MEM[PC])
            if(a != 0):
                PC = a
                f1 = 1
            dictionary_of_reg_binary["FLAGS"]='0'*16
        
        elif opcode=="10000": #this is for the F_ADDITION
            addf(MEM[PC])
        
        elif opcode == "10001":
            subf(MEM[PC])
        
        elif opcode == "10010":
            movf(MEM[PC])
            
            
        
            
            
    a = bin(PC_PRINTED)
    a1 = ('0'*(7-len(a[2:]))) + str(a[2:])
    PC_PRINTED+=1
    if(f1==0):
        PC += 1
    #a2 = [('0'*(16-len(bin(register_values[i])[2:])))+bin(register_values[i])[2:] for i in register_values.keys()]
    #a1.extend(a2)
    print(a1+"        "+dictionary_of_reg_binary["R0"]+" "+dictionary_of_reg_binary["R1"]+" "+dictionary_of_reg_binary["R2"]+" "+dictionary_of_reg_binary["R3"]+" "+dictionary_of_reg_binary["R4"]+" "+dictionary_of_reg_binary["R5"]+" "+dictionary_of_reg_binary["R6"]+" "+dictionary_of_reg_binary["FLAGS"]+" ")


# For the memory Dump after the execution of all lines have ended.    
j=0    


for i in MEM:
    print(i)
    j+=1
for g in dictionary_of_label_addresses_decimal:
    print((16-len(bin(dictionary_of_label_addresses_decimal[g])[2:]))*'0'+bin(dictionary_of_label_addresses_decimal[g])[2:])
    j+=1
while(j!=128):
    print('0'*16)
    j+=1
        
    
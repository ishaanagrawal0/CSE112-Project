'''
Aditya Gupta 2022031
Debjit Banerji 2022146
Himang Chandra Garg 2022214
Ishaan Agrawal 2022221
'''
dictionary_of_variables={} #dictionary to store the variables
operations = {
    'add' : '00000',
    'sub' : '00001',
    'movI' : '00010', #Need changes here
    'movR' : '00011',
    'ld' : '00100',
    'st' : '00101',
    'mul' : '00110',
    'div' : '00111',
    'rs' : '01000',
    'ls' : '01001',
    'xor' : '01010',
    'or':'01011',
    'and' : '01100',
    'not':'01101',
    'cmp' : '01110',
    'jmp' : '01111',
    'jlt' : '11100',
    'jgt' : '11101',
    'je' : '11111',
    'hlt' : '11010',
}
#7 registers and one flag register we have in the question
registers={
    "R0":"000",
    "R1":"001",
    "R2":"010",
    "R3":"011", 
    "R4":"100",
    "R5":"101",
    "R6":"110",
    "FLAGS":"111"
}
dictionary_of_reg_values={}  #to store the values of the registers in the dictionary
dictionary_of_reg_binary={}  #to store the binary values of the registers(16 bits)

flags="0"*16

f1=0 #Flag to check whether halt instruction was read or not

dictionary_of_label_addresses_decimal={}

list_of_variables=[]
#Empty line: Ignore these lines
#A label
#An instruction
#A variable definition
f1=open(r"C:\Users\adity\Downloads\stdin.txt","r")
lines=f1.readlines()

def MoveImmediate(reg1,Imm):
    #format is mov reg1 $Imm
    s="00010"
    Imm=int(Imm)
    s+="0" #unused bits
    s+=registers[reg1]
    x=str(bin(Imm)[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def MoveRegister(reg1,reg2):
    #format is mov reg1 reg2
    s="00011"
    s+="0"*5
    s+=registers[reg1]
    s+=registers[reg2]
    return s

def Addition(reg1,reg2,reg3):
    #format is reg1=reg2+reg3
    s="00000"
    s+="00"#unused bits
    s+=registers[reg1]
    s+=registers[reg2]
    s+=registers[reg3]
    
    return s

def Subtraction(reg1,reg2,reg3):
    #format is reg1=reg2-reg3
    s="00001"
    s+="00" #unused bits
    s+=registers[reg1]
    s+=registers[reg2]
    s+=registers[reg3]
    
    return s

def Load(reg1,Mem_addr):
    #format is ld reg1 mem_addr
    s="00100"
    s+="0"
    s+=registers[reg1]
    s+=dictionary_of_variables[Mem_addr]
    return s

def Store(reg1,Mem_addr):
    s="00101"
    s+="0"
    s+=registers[reg1]
    s+=dictionary_of_variables[Mem_addr]
    return s

def Multiply(reg1,reg2,reg3):
    #format is reg1=reg2.reg3
    s="00110"
    s+="00" #unused bits
    s+=registers[reg1]
    s+=registers[reg2]
    s+=registers[reg3]
    
    return s

def Divide(reg3,reg4):
    s="00111"
    s+="0"*5
    s+=registers[reg3]
    s+=registers[reg4]
    return s

def Right_Shift(reg1,Imm):
    #format is rs reg1 $Imm
    s="01000"   
    s+="0"
    s+=registers[reg1]
    Imm_1=int(Imm)
    x=str(bin(Imm_1)[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Left_Shift(reg1,Imm):
    #format is ls reg1 $Imm 
    s="01001"
    s+="0"
    s+=registers[reg1]
    Imm=int(Imm)
    x=str(bin(Imm)[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def ExclusiveOR(reg1,reg2,reg3):
    #format is reg1=reg2^reg3
    s="01010"
    s+="00" #unused bits
    s+=registers[reg1]
    s+=registers[reg2]
    s+=registers[reg3]
    
    return s

def Or(reg1,reg2,reg3):
    #format is reg1=reg2|reg3
    s="01011"
    s+="00" #unused bits
    s+=registers[reg1]
    s+=registers[reg2]
    s+=registers[reg3]
    
    return s

def And(reg1,reg2,reg3):
    #format is reg1=reg2|reg3
    s="01100"
    s+="00" #unused bits
    s+=registers[reg1]
    s+=registers[reg2]
    s+=registers[reg3]
    
    return s
    
def Invert(reg1,reg2):
    #format is not reg1 reg2
    s="01101"
    s+="0"*5
    s+=registers[reg1]
    s+=registers[reg2] 
    return s

def Compare(reg1,reg2):
    s="01110"
    s+="0"*5
    s+=registers[reg1]
    s+=registers[reg2]
    return s

def Unconditonal_Jump(Mem_addr):
    #format is jmp mem_addr
    s="01111"
    s+="0"*4
    x=str(bin(Mem_addr)[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Jump_If_Less_Than(Mem_addr):
    s="11100"
    s+="0"*4
    x=str(bin(Mem_addr)[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Jump_If_Greater_Than(Mem_addr):
    s="11101"
    s+="0"*4
    x=str(bin(Mem_addr)[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Jump_If_Equal(Mem_addr):
    s="11111"
    s+="0"*4
    x=str(bin(Mem_addr)[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Halt():
    s="11010"
    s+="0"*11
    return s

# Function to check whether the name of register is correct or not
def check_reg(reg1):
    if(reg1 in registers) and(reg1!="FLAGS"):
        return 1
    return 0

number_of_instructions=0
for line in lines:
    line=line.strip().replace("\n","")
    words=line.split(" ")
    if words[0]!="var":
        number_of_instructions+=1
    if words[0]=="hlt":
        break
    if words[0][-1]==":":
        dictionary_of_label_addresses_decimal[words[:-1]]=number_of_instructions-1

for line in lines:
    line=line.strip().replace("\n","")
    words=line.split(" ")
    
    if (f1==1):
        print("Error - Halt not used as last instruction")
        break
    
    if words[0]=="var":
        l=number_of_instructions #as the first memory addr is 0
        dictionary_of_variables[words[1]]=bin(l)[2:] #as the mem_addr is of 7 bits only
        dictionary_of_variables[words[1]]="0"*(7-len(dictionary_of_variables[words[1]]))+dictionary_of_variables[words[1]]
        number_of_instructions+=1
        
    elif words[0]=="mov":
        if "$" in words[2]:
            #the $Imm is of 7 bits only thus is should not be more than 127
            dictionary_of_reg_values[words[1]]=int(words[2][1:])
            dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
            dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
            print(MoveImmediate(words[1],words[2][1:]))
            
        else:
            dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]
            dictionary_of_reg_binary[words[1]]=dictionary_of_reg_binary[words[2]]
            print(MoveRegister(words[1],words[2]))
    
    elif words[0]="ld":
        if(words[2] not in dictionary_of_variables):
            print("Error - Invalid Variable Name")
            break
        print(Load(words[1],words[2]))
        
    elif words[0]=="st":
        if(words[2] not in dictionary_of_variables):
            print("Error - Invalid Variable Name")
            break
        print(Store(words[1],words[2]))
    
    #TYPE A COMMANDS
    
    elif words[0]=="add":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]+dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Addition(words[1],words[2],words[3]))
        
    elif words[0]=="sub":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]-dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Subtraction(words[1],words[2],words[3]))

    elif words[0]=="mul":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]*dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Multiply(words[1],words[2],words[3]))
        
    elif words[0]=="div":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[1]]//dictionary_of_reg_values[words[2]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Divide(words[1],words[2]))
        
    elif words[0]=="rs":
        i=int(words[2][1:])
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[1]]>>i
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Right_Shift(words[1],words[2][1:]))
        
    elif words[0]=="ls":
        i=int(words[2][1:])
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[1]]<<i
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Left_Shift(words[1],words[2][1:]))
    
    elif words[0]=="xor":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]^dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(ExclusiveOR(words[1],words[2],words[3]))
    
    elif words[0]=="or":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]|dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Or(words[1],words[2],words[3]))
    
    elif words[0]=="and":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]&dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(And(words[1],words[2],words[3]))
    
    elif words[0]=="not":
        dictionary_of_reg_values[words[1]] = ~(dictionary_of_reg_values[words[2]])
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Invert(words[1],words[2]))
        
    elif words[0]=="cmp":
        if(dictionary_of_reg_values[words[1]]==dictionary_of_reg_values[words[2]]):
            flags = flags[:15] + "1"
        elif(dictionary_of_reg_values[words[1]]>dictionary_of_reg_values[words[2]]):
            flags = flags[:14] + "1" + flags[15]
        else:
            flags = flags[:13] + "1" + flags[14:]
        print(Compare(words[1],words[2]))
    
    elif words[0][0]=="j":
        if(words[0]=="jmp" and words[1] in dictionary_of_label_addresses_decimal):
            print(Unconditional_Jump(dictionary_of_label_addresses_decimal[words[1]]))
        elif(words[0]=="jlt" and words[1] in dictionary_of_label_addresses_decimal):
            print(Jump_If_Less_Than(dictionary_of_label_addresses_decimal[words[1]]))
        elif(words[0]=="jgt" and words[1] in dictionary_of_label_addresses_decimal):
            print(Jump_If_Greater_Than(dictionary_of_label_addresses_decimal[words[1]]))
        elif(words[0]=="je" and words[1] in dictionary_of_label_addresses_decimal):
            print(Jump_If_Equal(dictionary_of_label_addresses_decimal[words[1]]))
        else:
             print("Syntax Error!")
             break
        
    elif words[0]=="hlt":
        f1=1
        print(Halt())
         
    else:
        print("Syntax Error!")
    
# Create separate if else blocks to check for valid register names for command types - A,B,C,D

print(dictionary_of_variables)
print(dictionary_of_reg_values)
print(dictionary_of_reg_binary)
    

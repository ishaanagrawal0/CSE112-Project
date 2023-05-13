'''
Aditya Gupta 2022031
Debjit Banerji 2022146
Himang Chandra Garg 2022214
Ishaan Agrawal 2022221
'''

dictionary_of_variables={} #dictionary to store the variables

#7 registers and one flag register we have in the question
registers={
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011", 
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111"
}
dictionary_of_reg_values={}  #to store the values of the registers in the dictionary
dictionary_of_reg_binary={}  #to store the binary values of the registers(16 bits)

flags="0"*16  # initial value of flag is of form 000000000000/0000

halt_finder=0 #Flag to check whether halt instruction was read or not

MAX_INT=(2**16-1)
dictionary_of_label_addresses_decimal={}

list_of_variables=[]
#Empty line: Ignore these lines
#A label
#An instruction
#A variable definition
f1=open(r"stdin.txt","r")
lines=f1.readlines()
f1.close()

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
    #if len(x)>7:
    #    s=f"ERROR-the immediate value has more than 7 bits-(line no.{i})"
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
    #cmp reg1 reg2
    s="01110"
    s+="0"*5
    s+=registers[reg1]
    s+=registers[reg2]
    return s

def Unconditonal_Jump(Mem_addr):
    #format is jmp mem_addr
    s="01111"
    s+="0"*4
    x=str(bin(dictionary_of_label_addresses_decimal[Mem_addr])[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Jump_If_Less_Than(Mem_addr):
    #format is jlt mem_addr
    s="11100"
    s+="0"*4
    x=str(bin(dictionary_of_label_addresses_decimal[Mem_addr])[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Jump_If_Greater_Than(Mem_addr):
    #jgt mem_addr
    s="11101"
    s+="0"*4
    x=str(bin(dictionary_of_label_addresses_decimal[Mem_addr])[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Jump_If_Equal(Mem_addr):
    #je mem_addr
    s="11111"
    s+="0"*4
    x=str(bin(dictionary_of_label_addresses_decimal[Mem_addr])[2:])
    while len(x)<7:
        x="0"+x
    s+=x
    return s

def Halt():
    #hlt
    s="11010"
    s+="0"*11
    return s

# Function to check whether the name of register is correct or not
def check_reg(reg1):
    if (reg1 in registers) and(reg1!="FLAGS"):
        return 1
    return 0

number_of_instructions=0
normal_instruction_flag=0

f2 = open("stdout.txt","w")

for line in lines:
    line=" ".join(line.split())
    line=line.strip().replace("\n","")
    words=line.split(" ")
    if words[0]!="var":
        normal_instruction_flag=1
        number_of_instructions+=1
    else:
        if(words[0]=="var" and normal_instruction_flag==1):
            print("Error - All variables not declared at the beginning! (Line No.: "+str(number_of_instructions)+")")    
    if words[0]=="hlt":
        break
    if words[0][-1]==":":
        dictionary_of_label_addresses_decimal[words[0][:-1]] =number_of_instructions-1
        
i=0 # Line counter
for line in lines:
    #sprint(line)
    line = line.strip().replace("\n", "")
    words = line.split()  # Splitting without specifying a delimiter to split on whitespace
    # Rest of your code to process the words

    
    if (halt_finder==1):  #correct
        print("Error - Halt not used as last instruction (Line No.: "+str(i)+")")
        
    
    if words[0] in ["add","sub","mul","xor","or","and"]:
       if(not(check_reg(words[1])) and not(check_reg(words[2])) and not(check_reg(words[3]))):
        print("Error - Use of invalid register(s) (Line No.: "+str(i)+")")
        i+=1
        continue
    elif words[0] in ["rs","ls"]:
        if(not(check_reg(words[1]))):
            print("Error - Use of invalid register(s) (Line No.: "+str(i)+")")
            i+=1
            continue
    elif words[0] in ["div","not","cmp"]:
        if(not(check_reg(words[1])) and not(check_reg(words[2]))):
            print("Error - Use of invalid register(s) (Line No.: "+str(i)+")")
            i+=1
            continue
    elif words[0] in ["ld","st"]:
        if(not(check_reg(words[1]))):
            print("Error - Use of invalid register(s) (Line No.: "+str(i)+")")
            i+=1
            continue
        
    
    if words[0]=="var":
        l=number_of_instructions #as the first memory addr is 0
        dictionary_of_variables[words[1]]=bin(l)[2:] #as the mem_addr is of 7 bits only
        dictionary_of_variables[words[1]]="0"*(7-len(dictionary_of_variables[words[1]]))+dictionary_of_variables[words[1]]
        number_of_instructions+=1
        
    elif words[0]=="mov":
        if "$" in words[2]:
            if check_reg(words[1]):
                #the $Imm is of 7 bits only thus is should not be more than 127
                dictionary_of_reg_values[words[1]]=int(words[2][1:])
                dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
                dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
                var = MoveImmediate(words[1],words[2][1:])
                print(var)
                if var[0:5] != 'ERROR':
                    f2.write(var)
                    f2.write("\n")
            else:
                print("Error - Use of invalid register! (Line No.: "+str(i)+")")              
            
        else:
            if (check_reg(words[1]) and check_reg(words[2])):
                dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]
                dictionary_of_reg_binary[words[1]]=dictionary_of_reg_binary[words[2]]
                print(MoveRegister(words[1],words[2]))
                f2.write(MoveRegister(words[1],words[2]))
                f2.write("\n")
            else:
                print("Error - Use of invalid register! (Line No.: "+str(i)+")")
    
    elif words[0]=="ld":
        if(words[2] not in dictionary_of_variables):
            print("Error - Invalid Variable Name")
            break
        dictionary_of_reg_values[words[1]]=0 #storing the default value to 0 for loading from a memory location
        print(Load(words[1],words[2]))
        f2.write(Load(words[1],words[2]))
        f2.write("\n")
        
    elif words[0]=="st":
        if(words[2] not in dictionary_of_variables):
            print("Error - Invalid Variable Name")
            break
        if words[1] not in dictionary_of_reg_values:
            dictionary_of_reg_values[words[1]]=0
    
        print(Store(words[1],words[2]))
        f2.write(Store(words[1],words[2]))
        f2.write("\n")
    
    #TYPE A COMMANDS
    
    elif words[0]=="add":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]+dictionary_of_reg_values[words[3]]
        if  dictionary_of_reg_values[words[1]]>(MAX_INT):
            dictionary_of_reg_values[words[1]]=0
            flags="0"*(12)+"1"+"0"*(3)
        else:
            flags="0"*16 # reset to zero
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Addition(words[1],words[2],words[3]))
        f2.write(Addition(words[1],words[2],words[3]))
        f2.write("\n")
        
    elif words[0]=="sub":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]-dictionary_of_reg_values[words[3]]
        if dictionary_of_reg_values[words[1]]<0:
            dictionary_of_reg_values[words[1]]=0
            flags="0"*(12)+"1"+"0"*(3)
        else:
            flags="0"*16 # reset to zero
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Subtraction(words[1],words[2],words[3]))
        f2.write(Subtraction(words[1],words[2],words[3]))
        f2.write("\n")

    elif words[0]=="mul":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]*dictionary_of_reg_values[words[3]]
        if  dictionary_of_reg_values[words[1]]>(MAX_INT):
            dictionary_of_reg_values[words[1]]=0
            flags="0"*(12)+"1"+"0"*(3)
        else:
            flags="0"*16 # reset to zero
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Multiply(words[1],words[2],words[3]))
        f2.write(Multiply(words[1],words[2],words[3]))
        f2.write("\n")
        
    elif words[0]=="div":
        if dictionary_of_reg_values[words[2]]==0:
            dictionary_of_reg_values["R0"]=0
            dictionary_of_reg_values["R1"]=0
            flags="0"*(12)+"1"+"0"*(3)
        else:
            flags="0"*16
        dictionary_of_reg_values["R0"]=dictionary_of_reg_values[words[1]]//dictionary_of_reg_values[words[2]]
        dictionary_of_reg_values["R1"]=dictionary_of_reg_values[words[1]]%dictionary_of_reg_values[words[2]]
        dictionary_of_reg_binary["R0"]=str(bin(dictionary_of_reg_values["R0"])[2:])
        dictionary_of_reg_binary["R0"]="0"*(16-len(dictionary_of_reg_binary["R0"]))+dictionary_of_reg_binary[words[1]]
        dictionary_of_reg_binary["R1"]=str(bin(dictionary_of_reg_values["R1"])[2:])
        dictionary_of_reg_binary["R1"]="0"*(16-len(dictionary_of_reg_binary["R1"]))+dictionary_of_reg_binary[words[1]]
        print(Divide(words[1],words[2]))
        f2.write(Divide(words[1],words[2]))
        f2.write("\n")
        
    elif words[0]=="rs":
        i=int(words[2][1:])
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[1]]>>i
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Right_Shift(words[1],words[2][1:]))
        f2.write(Right_Shift(words[1],words[2][1:]))
        f2.write("\n")
        
    elif words[0]=="ls":
        i=int(words[2][1:])
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[1]]<<i
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Left_Shift(words[1],words[2][1:]))
        f2.write(Left_Shift(words[1],words[2][1:]))
        f2.write("\n")
    
    elif words[0]=="xor":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]^dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(ExclusiveOR(words[1],words[2],words[3]))
        f2.write(ExclusiveOR(words[1],words[2],words[3]))
        f2.write("\n")
    
    elif words[0]=="or":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]|dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Or(words[1],words[2],words[3]))
        f2.write(Or(words[1],words[2],words[3]))
        f2.write("\n")

    elif words[0]=="and":
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]&dictionary_of_reg_values[words[3]]
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(And(words[1],words[2],words[3]))
        f2.write(And(words[1],words[2],words[3]))
        f2.write("\n")
    
    elif words[0]=="not":
        dictionary_of_reg_values[words[1]] = ~(dictionary_of_reg_values[words[2]])
        dictionary_of_reg_binary[words[1]]=str(bin(dictionary_of_reg_values[words[1]])[2:])
        dictionary_of_reg_binary[words[1]]="0"*(16-len(dictionary_of_reg_binary[words[1]]))+dictionary_of_reg_binary[words[1]]
        print(Invert(words[1],words[2]))
        f2.write(Invert(words[1],words[2]))
        f2.write("\n")
        
    elif words[0]=="cmp":
        if(dictionary_of_reg_values[words[1]]==dictionary_of_reg_values[words[2]]):
            flags = "0"*15 + "1"
        elif(dictionary_of_reg_values[words[1]]>dictionary_of_reg_values[words[2]]):
            flags = "0"*14 + "1" + "0"
        else:
            flags = "0"*13 + "1" + "0"*2
        print(Compare(words[1],words[2]))
        f2.write(Compare(words[1],words[2]))
        f2.write("\n")
    
    elif words[0][0]=="j":
        if(words[0]=="jmp" and words[1] in dictionary_of_label_addresses_decimal):
            print(Unconditonal_Jump(words[1]))   
        elif(words[0]=="jlt") and (words[1] in dictionary_of_label_addresses_decimal) :#and flags[13]==1:
            print(Jump_If_Less_Than(dictionary_of_label_addresses_decimal[words[1]]))   
        elif(words[0]=="jgt") and (words[1] in dictionary_of_label_addresses_decimal) :#and flags[14]==1:
            print(Jump_If_Greater_Than(words[1]))
        elif(words[0]=="je") and (words[1] in dictionary_of_label_addresses_decimal) :#and flags[15]==1:
            print(Jump_If_Equal(words[1]))
            f2.write(Jump_If_Equal(words[1]))
            f2.write("\n")
            
        else:
            print("Error - Use of undefined labels! (Line No.: "+str(i)+")")
        
    elif words[0]=="hlt":
        halt_finder=1
        print(Halt())
        f2.write(Halt())
    
    elif ":" in words[0]:
        s=words[1:]
        s1=""
        for x in s:
            s1=s1+x+" "
        lines.insert(i + 1, s1)
    else:
        print("Syntax Error!")
    i+=1

if halt_finder!=1:
    print("Error - Halt Instruction missing in the code")
    
# Create separate if else blocks to check for valid register names for command types - A,B,C,D

f2.close()

print(dictionary_of_variables)
print(dictionary_of_label_addresses_decimal)
print(dictionary_of_reg_values)
print(dictionary_of_reg_binary)

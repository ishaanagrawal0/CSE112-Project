'''
Aditya Gupta 2022031
Debjit Banerji 2022146
Himang Chandra Garg 2022214
Ishaan Agrawal 2022221
'''
import sys
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
dictionary_of_reg_values={"R0":0,"R1":0,'R2':0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":0}  #to store the values of the registers in the dictionary
dictionary_of_reg_binary={"R0":0,"R1":0,'R2':0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":0}  #to store the binary values of the registers(16 bits)

flags="0"*16  # initial value of flag is of form 000000000000/0000

halt_finder=0 #Flag to check whether halt instruction was read or not

MAX_INT=(2**16-1)
dictionary_of_label_addresses_decimal={}

    

list_of_variables=[]
#Empty line: Ignore these lines
#A label
#An instruction
#f1=open(r"C:\Users\adity\Downloads\stdin.txt",'r')
#lines=f1.readlines()
lines=sys.stdin.readlines()

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

# print(lines)
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


def movf(reg1,Imm):
    s = "10010" #no unused bit needed
    Imm=float(Imm)
    dictionary_of_reg_values[reg1]=Imm
    if Imm>1:
        exponent_part=0
    else:
        exponent_part= (-3)
    while(Imm//(2**(exponent_part))!=1):
        exponent_part+=1
    #print(exponent_part)

    number_left=(Imm/2**(exponent_part))-1
    #print(float_bin(number_left,5))
    mantissa=float_bin(number_left,5)
    s+= registers[reg1]
    exponent_part+=3 #adding the bias 
    s+= (3-len(bin(exponent_part)[2:]))*'0'+bin(exponent_part)[2:]
    s+= (mantissa)
    dictionary_of_reg_binary[reg1]='0'*8+(3-len(bin(exponent_part)[2:]))*'0'+bin(exponent_part)[2:]+mantissa
    return s
    

def addf(reg1,reg2,reg3):
    s = "10000"
    s += "0"*2
    s += registers[reg1]
    s += registers[reg2]
    s += registers[reg3]
    return s
def subf(reg1,reg2,reg3):
    s = "10001"
    s += "0"*2
    s += registers[reg1]
    s += registers[reg2]
    s += registers[reg3]
    return s
    
def Halt():
    #hlt
    s="11010"
    s+="0"*11
    return s

# Function to check whether the name of register is correct or not
def check_reg(reg1):
    if (reg1 in registers) and (reg1!="FLAGS"):
        return 1
    return 0

number_of_instructions=0
normal_instruction_flag=0

f2 = open("stdout.txt","w")

for line in lines:
    line=" ".join(line.split())
    line=line.strip().replace("\n","")
    words=line.split(" ")
    if words[0]=="":
        continue
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

    if words==[]:
        continue
    if (halt_finder==1):  #correct
        print("Error - Halt not used as last instruction (Line No.: "+str(i)+")")
     
    if words[0] in ["add","sub","mul","xor","or","and"]:
       if(not(check_reg(words[1])) or not(check_reg(words[2])) or not(check_reg(words[3]))):
        print("Error - Use of invalid register(s) (Line No.: "+str(i)+")")
        i+=1
        continue
    elif words[0] in ["rs","ls"]:
        if(not(check_reg(words[1]))):
            print("Error - Use of invalid register(s) (Line No.: "+str(i)+")")
            i+=1
            continue
    elif words[0] in ["div","not","cmp"]:
        if(not(check_reg(words[1])) or not(check_reg(words[2]))):
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
                if int(words[2][1:])>127:
                    print("error value more than 127")
                    exit()
                print(var)
                
                if var[0:5] != 'ERROR':
                    f2.write(var)
                    f2.write("\n")
            else:
                print("Error - Use of invalid register! (Line No.: "+str(i)+")")   
                halt_finder=1
                break           
            
        else:
            if check_reg(words[1]):
                dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[2]]
                dictionary_of_reg_binary[words[1]]=dictionary_of_reg_binary[words[2]]
                print(MoveRegister(words[1],words[2]))
                f2.write(MoveRegister(words[1],words[2]))
                f2.write("\n")
            else:
                print("Error - Use of invalid register! (Line No.: "+str(i)+")")
                halt_finder=1
                break
    
    elif words[0]=="ld":
        if(words[2] not in dictionary_of_variables):
            print("Error - Invalid Variable Name")
            halt_finder=1
            break
        dictionary_of_reg_values[words[1]]=0 #storing the default value to 0 for loading from a memory location
        print(Load(words[1],words[2]))
        f2.write(Load(words[1],words[2]))
        f2.write("\n")
        
    elif words[0]=="st":
        if(words[2] not in dictionary_of_variables):
            print("Error - Invalid Variable Name")
            halt_finder=1
            break
        if words[1] not in dictionary_of_reg_values:
            dictionary_of_reg_values[words[1]]=0
    
        print(Store(words[1],words[2]))
        f2.write(Store(words[1],words[2]))
        f2.write("\n")
    elif words[0] in ["addf","subf","movf"]: #Considering the range for exponent to be -3 to +4
            #print(words[2])
            #print(float(words[2][1:]))
        if words[0]=='movf':
            if (float(words[2][1:])>=0.125 and float(words[2][1:])<=31.5): #for the range of the floating point numbers
                print(movf(words[1],words[2][1:]))
            
            else:
                print("the immediate value of floating point is not in the correct bounds(1.5 to 31.5)")
            
        elif(words[0] == "addf"):
            if (words[1]!='FLAGS' and words[2]!='FLAGS' and words[3]!='FLAGS'):
                # Add the assert statement for checking whether any of the three registers is flags for addf and subf.
                if(dictionary_of_reg_values[words[2]]+dictionary_of_reg_values[words[3]] > 31.5): # By converting the binary 1.11111 x 2^4
                    dictionary_of_reg_binary["FLAGS"] = '0000000000001000'
                    dictionary_of_reg_values[words[1]] = 0
                    dictionary_of_reg_binary[words[1]] = "0"*16
                else:
                    dictionary_of_reg_values[words[1]] = dictionary_of_reg_values[words[2]] + dictionary_of_reg_values[words[3]]
    
                
                print(addf(words[1],words[2],words[3]))
                #f2.write(addf(words[1],words[2],words[3]))
            else:
                print("Error - FLAGS register cannot be used in the floating point addition operation.")
        elif(words[0] == "subf"):
            if (words[1]!='FLAGS' and words[2]!='FLAGS' and words[3]!='FLAGS'):
                if(dictionary_of_reg_values[words[2]] < dictionary_of_reg_values[words[3]]): # By converting the binary 1.11111 x 2^4
                    dictionary_of_reg_binary["FLAGS"] = '0000000000001000'
                    dictionary_of_reg_values[words[1]] = 0
                    dictionary_of_reg_binary[words[1]] = "0"*16
                else:
                    dictionary_of_reg_values[words[1]] = dictionary_of_reg_values[words[2]] - dictionary_of_reg_values[words[3]]
                
                print(subf(words[1],words[2],words[3]))
            else:
                print("Error - FLAGS register cannot be used in the floating point addition operation.")        
                
                
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
        #dictionary_of_reg_values["R0"]=dictionary_of_reg_values[words[1]]//dictionary_of_reg_values[words[2]]
        #dictionary_of_reg_values["R1"]=dictionary_of_reg_values[words[1]]%dictionary_of_reg_values[words[2]]
        #dictionary_of_reg_binary["R0"]=str(bin(dictionary_of_reg_values["R0"])[2:])
        #dictionary_of_reg_binary["R0"]="0"*(16-len(dictionary_of_reg_binary["R0"]))+dictionary_of_reg_binary[words[1]]
        #dictionary_of_reg_binary["R1"]=str(bin(dictionary_of_reg_values["R1"])[2:])
        #dictionary_of_reg_binary["R1"]="0"*(16-len(dictionary_of_reg_binary["R1"]))+dictionary_of_reg_binary[words[1]]
        print(Divide(words[1],words[2]))
        f2.write(Divide(words[1],words[2]))
        f2.write("\n")
        
    elif words[0]=="rs":
        n1=int(words[2][1:])
        dictionary_of_reg_values[words[1]]=dictionary_of_reg_values[words[1]]>>n1
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
        if words[1]=='hlt':
            halt_finder=1
            print(Halt())
            break
        s1=""
        for x in s:
            s1=s1+x+" "
        lines.insert(i + 1, s1)
    else:
        print("Syntax Error!")
        halt_finder=1
        break
    i+=1

if halt_finder!=1:
    print("Error - Halt Instruction missing in the code")
    
# Create separate if else blocks to check for valid register names for command types - A,B,C,D

#f2.close()

#print(dictionary_of_variables)
#print(dictionary_of_label_addresses_decimal)
#print(dictionary_of_reg_values)
#print(dictionary_of_reg_binarys)


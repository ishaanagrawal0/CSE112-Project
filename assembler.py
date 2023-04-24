'''
Aditya Gupta 2022031
Debjit Banerji 2022146
Himang Chandra Garg 2022214
Ishaan Agrawal 2022221
'''

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
#Empty line: Ignore these lines
#A label
#An instruction
#A variable definition
f1=open(r"C:\Users\adity\Downloads\stdin.txt","r")
lines=f1.readlines()
def Addition(reg1,reg2,reg3):
    #format is reg1=reg2+reg3
    s="00000"
    s+="00"#unused bits
    s+=registers[reg1]
    s+=registers[reg2]
    s+=registers[reg3]
    
    return s
    
    
for line in lines:
    line=line.replace("\n","")
    words=line.split(" ")
    if words[0]=="add":
        print(Addition(words[1],words[2],words[3])+"\n")
    
        

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

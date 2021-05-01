import os, sys

function = {"100000r": "add", "100001r": "addu", "001000i": "addi", "001001i": "addiu",
    "011010r": "div", "011011r": "divu", "011000r": "mult", "011001r": "multu",
    "100010r": "sub", "100011r": "subu", "100100r": "and", "001100i": "andi", "100111r": "nor",
    "100101r": "or", "001101i": "ori", "100110r": "xor", "001110i": "xori", "000000r": "sll",
    "000100r": "sllv", "000011r": "sra", "000111r": "srav", "000010r": "srl", "000110r": "srlv",
    "000100i": "beq", "000111i": "bgtz", "000110i": "blez", "000101i": "bne", "000010j": "j",
    "000011j": "jal", "001001r": "jalr", "001000r": "jr", "100000i": "lb", "100100i": "lbu",
    "100001i": "lh", "100101i": "lhu", "100011i": "lw", "101000i": "sb", "101001i": "sh",
    "101011i": "sw", "010000r": "mfhi", "010010r": "mflo", "101010r": "slt", "101001r": "sltu",
    "001010i": "slti", "001001i": "sltiu"}

register = {0: "$zero", 1: "$at", 2: "$v0", 3: "$v1", 4: "$a0", 5: "$a1", 6: "$a2", 7: "$a3",
8: "$t0", 9: "$t1", 10: "$t2", 11: "$t3", 12: "$t4", 13: "$t5", 14: "$t6", 15: "$t7",
16: "$s0", 17: "$s1", 18: "$s2", 19: "$s3", 20: "$s4", 21: "$s5", 22: "$s6", 23: "$s7",
24: "$t8", 25: "$t9", 26: "$k0", 27: "$k1", 28: "$gp", 29: "$sp", 30: "$fp", 31: "$ra"}

def decode(instruction: str):
    instruction = instruction.replace(" ", "")

    if instruction == "exit":
        print("\nClosing Script\n")
        sys.exit()

    if len(instruction) != 32 or not set(instruction).issubset({'0', '1'}):
        print("\nInvalid instruction: must enter 32-bit binary string\n")
        return
    
    opcode = instruction[:6]

    if opcode == "000000" and function.get(instruction[26:] + 'r', None):
        rs1 = instruction[6:11]
        rt2 = instruction[11:16]
        destination = instruction[16:21]
        shamt = instruction[21:26]
        funct = instruction[26:]

        print("\nR-TYPE", "\nOPCODE:", opcode,
        "\nRS:", rs1, "( register", int("0b"+rs1, 2), register.get(int("0b"+rs1, 2), "ERROR"), ")",
        "\nRT:", rt2, "( register", int("0b"+rt2, 2), register.get(int("0b"+rt2, 2), "ERROR"), ")",
        "\nDEST:", destination, "( register", int("0b"+destination, 2),
        register.get(int("0b"+destination, 2), "ERROR"),")",
        "\nSHAMT:", shamt, "(", int("0b"+shamt, 2), "bits )",
        "\nFUNCT:", funct, "(", function.get(funct + "r", "ERROR"), ")\n")

    elif function.get(opcode + 'i', None):
        rs1 = instruction[6:11]
        rt2 = instruction[11:16]
        immediate = instruction[16:]

        shift = int("0b" + immediate[2:] + "00", 2)
        if (shift & (1 << (16 - 1))) != 0:  # GET 2S COMPLEMENT
            shift = shift - (1 << 16)

        print("\nI-TYPE", "\nOPCODE:", opcode, "(", function.get(opcode + "i", "ERROR"), ")",
        "\nRS:", rs1, "( register", int("0b"+rs1, 2), register.get(int("0b"+rs1, 2), "ERROR"), ")",
        "\nRT:", rt2, "( register", int("0b"+rt2, 2), register.get(int("0b"+rt2, 2), "ERROR"), ")",
        "\nIMMED:", immediate, "(", int("0b"+immediate, 2), ")",
        "( With Shift", shift, ")\n")

    elif function.get(opcode + 'j', None):
        address = instruction[6:]
        print("\nJ-TYPE", "\nOPCODE:", opcode, "(", function.get(opcode + "j", "ERROR"), ")",
        "\nADR:", address, "(", int("0b"+address, 2), ")",
        "( With Shift", int("0b"+address, 2) << 2, ")\n")

    else:
        print("\nMIPS instruction not found\n")
    
    return

os.system('cls' if os.name=='nt' else 'clear')
print("SYNTAX: Instruction must be a 32-bit binary string")
print("Type 'exit' to close")
print("\n--------------------------------------------------\n")
while True:
    instruction = input("ENTER MIPS INSTRUCTION: ")
    decode(instruction)
    print("--------------------------------------------------\n")

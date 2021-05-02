"""
All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Anthony Tedja
"""

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

register = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1",  "$t2", 
"$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", 
"$s7", "$t8", "$t9", "$k0", "$k1", "$gp", "$sp", "$fp", "$ra"]


def decode(instruction: str):
    """ Decode MIPS instruction and print in shell.
    """
    instruction = instruction.replace(" ", "")

    if instruction == "exit":
        print("\nClosing Script\n")
        sys.exit()

    if len(instruction) != 32 or not set(instruction).issubset({'0', '1'}):
        print("\nInvalid instruction: must enter 32-bit binary string\n")
        return
    
    rsn, rtn = int("0b"+(rs := instruction[6:11]), 2), int("0b"+(rt := instruction[11:16]), 2)

    if not "1" in (opcode := instruction[:6]) and function.get((funct := instruction[26:]) + 'r', 0):
        destn, shamt = int("0b"+(destination := instruction[16:21]), 2), instruction[21:26]

        print("\nR-TYPE", "\nOPCODE:", opcode,
        "\nRS:", rs, "( register", rsn, register[rsn], ")",
        "\nRT:", rt, "( register", rtn, register[rtn], ")",
        "\nDEST:", destination, "( register", destn, register[destn], ")",
        "\nSHAMT:", shamt, "(", int("0b"+shamt, 2), "bits )",
        "\nFUNCT:", funct, "(", function.get(funct + "r"), ")\n")

    elif function.get(opcode + 'i', 0):
        immediate = instruction[16:]

        if ((shift := int("0b" + immediate[2:] + "00", 2)) & (1 << (16 - 1))) != 0:  # GET 2S
            shift = shift - (1 << 16)

        print("\nI-TYPE", "\nOPCODE:", opcode, "(", function.get(opcode + "i"), ")",
        "\nRS:", rs, "( register", rsn, register[rsn], ")",
        "\nRT:", rt, "( register", rtn, register[rtn], ")",
        "\nIMMED:", immediate, "(", int("0b"+immediate, 2), ")",
        "( With Shift", shift, ")\n")

    elif function.get(opcode + 'j', 0):
        adrn = int("0b" + (address := instruction[6:]), 2)
        
        print("\nJ-TYPE", "\nOPCODE:", opcode, "(", function.get(opcode + "j"), ")",
        "\nADR:", address, "(", adrn, ")",
        "( With Shift", adrn << 2, ")\n")

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

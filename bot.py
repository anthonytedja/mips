"""
All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Anthony Tedja
"""

import os

from discord.ext import commands
from dotenv import load_dotenv

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

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='decode', help='Decode 32-bit binary MIPS instruction')
async def decode(ctx, instruction=""):
    instruction = instruction.replace(" ", "")

    if len(instruction) != 32 or not set(instruction).issubset({'0', '1'}):
        await ctx.send("\nInvalid instruction: must enter 32-bit binary string\n")

    elif not "1" in (opcode := instruction[:6]) and function.get((funct := instruction[26:]) + 'r', 0):
        rsn, rtn = int("0b"+(rs := instruction[6:11]), 2), int("0b"+(rt := instruction[11:16]), 2)
        destn, shamt = int("0b"+(destination := instruction[16:21]), 2), instruction[21:26]

        val = f"\nR-TYPE\nOPCODE: {opcode}"
        val += f"\nRS: {rs} ( register {rsn} {register[rsn]} )\nRT: {rt} ( register {rtn} {register[rtn]} )"
        val += f"\nDEST: {destination} ( register {destn} {register[destn]} )"
        val += f"\nSHAMT: {shamt} ( {int('0b'+shamt, 2)} bits )"
        val += f"\nFUNCT: {funct} ( {function.get(funct + 'r')} )\n"
        await ctx.send(val)

    elif function.get(opcode + 'i', 0):
        rsn, rtn = int("0b"+(rs := instruction[6:11]), 2), int("0b"+(rt := instruction[11:16]), 2)
        immediate = instruction[16:]

        if ((shift := int("0b" + immediate[2:] + "00", 2)) & (1 << (16 - 1))) != 0:  # GET 2S
            shift = shift - (1 << 16)

        val = f"\nI-TYPE\nOPCODE: {opcode} ( {function.get(opcode + 'i')} )"
        val += f"\nRS: {rs} ( register {rsn} {register[rsn]} )"
        val += f"\nRT: {rt} ( register {rtn} {register[rtn]} )"
        val += f"\nIMMED: {immediate} ( {int('0b'+immediate, 2)} )"
        val += f"( With Shift {shift} )\n"
        await ctx.send(val)

    elif function.get(opcode + 'j', 0):
        adrn = int("0b" + (address := instruction[6:]), 2)
        
        val = f"\nJ-TYPE\nOPCODE: {opcode} ( {function.get(opcode + 'j')} )"
        val += f"\nADR: {address} ( {adrn} ) ( With Shift {adrn << 2} )\n"
        await ctx.send(val)

    else:
        await ctx.send("\nMIPS instruction not found\n")

bot.run(TOKEN)
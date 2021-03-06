# mips

[![Preview](assets/img/mips.jpg)](https://anthonytedja.github.io/mips)

> mips is a webpage, script, and discord bot that decompiles binary instructions into [`MIPS Assembly.`](https://en.wikibooks.org/wiki/MIPS_Assembly/Instruction_Formats)

## Script Usage

```cpp
SYNTAX: Instruction must be a 32-bit binary string
Type 'exit' to close

--------------------------------------------------

ENTER MIPS INSTRUCTION: 00001000 11010001 00000000 00100110

J-TYPE
OPCODE: 000010 ( j )
ADR: 00110100010000000000100110 ( 13697062 ) ( With Shift 54788248 )

--------------------------------------------------

ENTER MIPS INSTRUCTION: 00010101001001111111111111001101

I-TYPE
OPCODE: 000101 ( bne )
RS: 01001 ( register 9 $t1 )
RT: 00111 ( register 7 $a3 )
IMMED: 1111111111001101 ( 65485 ) ( With Shift -204 )

--------------------------------------------------   

ENTER MIPS INSTRUCTION: 0000 0000 1011 0001 0001 0000 0000 0010

R-TYPE 
OPCODE: 000000
RS: 00101 ( register 5 $a1 )
RT: 10001 ( register 17 $s1 )
DEST: 00010 ( register 2 $v0 )
SHAMT: 00000 ( 0 bits )
FUNCT: 000010 ( srl )

--------------------------------------------------

ENTER MIPS INSTRUCTION: exit

Closing Script
```

cd into `mips` and run `python decode.py` command or open [`decode.py`](https://github.com/anthonytedja/mips/blob/main/decode.py) to run the script. Requires [`python 3.8+`](https://docs.python.org/3/whatsnew/3.8.html)

- For the discord bot functionality, add the discord token in the `.env` file and use the bot.py file

## Features

- Local Storage saves last instruction

## Built With

- Bootstrap Studio
- Visual Studio Code

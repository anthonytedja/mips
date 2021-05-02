# mips

mips is a python-based script that decodes MIPS instructions.

## Usage

cd into `/mips` and run command or simply open `decode.py` to run the script

```cpp
python decode.py
```

## Examples

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

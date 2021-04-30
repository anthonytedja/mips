# mips

mips is a python-based script that decodes MIPS instructions.

## Usage

cd into the folder and run with python or simply open `decode.py` to run the script

```cpp
& C:/Python39/python.exe "c:/Users/Anthony Tedja/Documents/mips/decode.py"
```

## Examples

```cpp
SYNTAX: Instruction must be a 32-bit string followed by type "r", "i", or "j"
Type 'exit' to close

Enter MIPS instruction followed by the instruction type: 00001000 11010001 00000000 00100110 j    

J-TYPE
OPCODE: 000010 ( j )
ADR: 00110100010000000000100110 ( 13697062 ) ( With Shift 54788248 )

Enter MIPS instruction followed by the instruction type: 00010101001001111111111111001101 i

I-TYPE
OPCODE: 000101 ( bne )
RS: 01001 ( register 9 $t1 )
RT: 00111 ( register 7 $a3 )
IMMED: 1111111111001101 ( 65485 ) ( With Shift -204 )

Enter MIPS instruction followed by the instruction type: 0000 0000 1011 0001 0001 0000 0000 0010 r

R-TYPE
OPCODE: 000000
RS: 00101 ( register 5 $a1 )
RT: 10001 ( register 17 $s1 )
DEST: 00010 ( register 2 $v0 )
SHAMT: 00000 ( 0 bits )
FUNCT: 000010 ( srl )

Enter MIPS instruction followed by the instruction type: exit

Closing Script

PS C:\Users\Anthony Tedja\Documents\mips>
```

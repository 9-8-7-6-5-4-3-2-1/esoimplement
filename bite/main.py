# -*- coding: utf-8 -*-

# 17. https://esolangs.org/wiki/BITE

import sys

leftpad = (lambda string,number,char=' ':((number-len(string))*char)+string)
strshift = (lambda string,number:string[number:]+string[:number])


def bite(code,halt=False):
    code = leftpad(bin(ord(code[0])%256)[2:],8,'0')
    index = 0; count = 0
    while True:
        if count>64 and halt: print("Infinite Loop"); return
        if max(code[index],code[(index+1) % 8])=='0': break
        if code[index] == "1": code = strshift(code,1)
        index = (index+2)%8; count+=1
    print(end=chr(int(code,base=2)))

def main():
    if len(sys.argv) == 1: bite(sys.stdin.read(1));return
    elif '-detect' in sys.argv: bite(sys.stdin.read(1),True)
    elif len(sys.argv) == 2: bite(sys.argv[1]) if len(sys.argv[1]) else bite(open(sys.argv[1]).read())
    else: bite(sys.argv[1],sys.argv[2]=='detect')

if __name__ == '__main__':main()

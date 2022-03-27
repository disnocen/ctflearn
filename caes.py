#!/usr/bin/env python3
string="kxn iye lbedec"

letters="abcdefghijklmnopqrstuvwxyz"
letters_sub="defghijklmnopqrstuvwxyzabc"
new=''
for i in range(len(string)):
    char=string[i]
    # print(char)
    if char != ' ':
        index = letters_sub.index(char)
        new+=letters[i]
    else:
        new+=' '
print(new)


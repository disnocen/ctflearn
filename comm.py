string = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"

string = string.split()
new = ''
for i in range(len(string)):
    new+= (chr(int(string[i],16)))

print(new)

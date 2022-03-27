string = "0xc4115 0x4cf8"
string2 = "0xc41154cf8"
string = string.split()

a = (int(string[0],16))
b = (int(string[1],16))

print(a,string[0])
print(b,string[1])
print("========")
c=a+b
d=a-b
e=b-a
f=a*b
print(c,hex(c))
print(d,hex(d))
print(e,hex(e))
print(f,hex(f))

print(xor(a,b))

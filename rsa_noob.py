import base64
# e= 1
# c= 9327565722767258308650643213344542404592011161659991421
# n= 245841236512478852752909734912575581815967630033049838269083
def invmod(x,mod):
    d=pow(x,-1,mod)
    assert(x*d %mod == 1)
    return d
def decrypt_rsa(c,d,n):
    return pow(c,d,n)

def tests():
    assert(invmod(4,7) == 2)
e= 3
c= 219878849218803628752496734037301843801487889344508611639028
n= 245841236512478852752909734912575581815967630033049838269083

print()
print("nbits o n is {}".format(n.bit_length()))
print("invmode")
d=invmod(e,n)
# print("inv of {} mod {} is {}".format(e,n,d))
# print(tests())
print("decrypt")
m = decrypt_rsa(c,d,n)
print("m = {}".format(m))
print("creating bytes")
m_bytes_hex = bytes.fromhex(hex(m%n)[2:])
#encode m into a base64 encoded string
m_bytes= str(m%n).encode()
m_bytes_b64enc = base64.b64encode(m_bytes)
m_bytes_b64dec = base64.b64decode(m_bytes)

print(m_bytes_hex)
print(m_bytes_b64enc)
print(m_bytes_b64dec)

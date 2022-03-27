strr="ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB"

n = ""
n2 = ""
print()
for i in range(len(strr)):
    if i%8==0:
        n+=" "
        n2+=" "
    if strr[i] == "A":
        n+="0"
        n2+="1"
    else:
        n2+="0"
        n+="1"

print(n2)
print(n)

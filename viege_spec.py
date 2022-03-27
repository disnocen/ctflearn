
plain="attackatdawn"
word="lemon"
keyword=word
cyphertext="LXFOPVEFRNHR".lower()
letters="abcdefghijklmnopqrstuvwxyz"


# repeat word until it is same length of plain text
keyword = ''
for i in range(len(plain)):
    keyword += word[i%len(word)]

print(" ".join(plain))
print(" ".join(keyword))


#encrypt
cyphertext2 = ''
for i in range(len(plain)):
    cyphertext2 += letters[(letters.index(plain[i])+letters.index(keyword[i]))%26]

print("cyphertext2 is {}".format(cyphertext2))
print("cyphertext is {}".format(cyphertext))

print("cyphers equal? {}".format(cyphertext2==cyphertext))

#decrypt
plain2 = ''
for i in range(len(cyphertext)):
    plain2 += letters[(letters.index(cyphertext[i])-letters.index(keyword[i]))%26]

print("plain2 is {}".format(plain2))
print("plain is {}".format(plain))


print("plain equal? {}".format(plain2==plain))
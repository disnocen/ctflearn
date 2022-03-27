
plain="attackatdawn"
word="blorpy"
keyword=word
cyphertext="gwoxRgqssihYspOntqpxs"
letters="abcdefghijklmnopqrstuvwxyz"
letters += letters.upper()


# repeat word until it is same length of plain text
keyword = ''
for i in range(len(cyphertext)):
    keyword += word[i%len(word)]

print(" ".join(cyphertext))
print(" ".join(keyword))


#encrypt
# cyphertext2 = ''
# for i in range(len(plain)):
#     cyphertext2 += letters[(letters.index(plain[i])+letters.index(keyword[i]))%26]

# print("cyphertext2 is {}".format(cyphertext2))
# print("cyphertext is {}".format(cyphertext))

# print("cyphers equal? {}".format(cyphertext2==cyphertext))

#decrypt
plain2 = ''
for i in range(len(cyphertext)):
    if cyphertext[i] in letters:
        plain2 += letters[(letters.index(cyphertext[i])-letters.index(keyword[i]))%len(letters)]
    # else:
    #     plain2 +=cyphertext[i]

print("plain2 is {}".format(plain2))


# print("plain equal? {}".format(plain2==plain))

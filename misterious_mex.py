photo_data= ["qwert","yuiop","asdfg","hklzx","cvbnm"]
# create matrix for hill system
hill_matrix =[]
for i in range(len(photo_data)):
    row = []
    for j in range(len(photo_data[i])):
        row.append(ord



letter = "qwertyuiopasdfghklzxcvbnm"
alphabet = "abcdefghiklmnopqrstuvwxyz"
string_data='MQDzqdor{Ix4Oa41W_1F_B00h_m1YlqPpPP}'

new =""
for i in string_data:
    if i in letter:
        new+=alphabet[letter.index(i)]
    elif i in letter.upper():
        new+=alphabet[letter.upper().index(i)]
    else:
        new+= i

print(new)

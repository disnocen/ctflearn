string="01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"

new_string = ''
for i in range(len(string)):
    new_string += str((int(string[i]) +1) %2)

print_string = ''

for j in range(0,len(new_string),8):
    char_new = chr(int(string[j:j+8],2))
    print_string += char_new
    print(char_new)

print(print_string)


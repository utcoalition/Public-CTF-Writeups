s = ']_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA'
a = ''

for letter in s:
    a += chr(ord(letter) ^ 0x3c)

print(a)

from pwn import *
f=open('image.bmp','rb')
xx=f.readlines()
lol=xor(xx,'matrix')
f1=open('solved.bmp','wb')
f1.write(lol)
f1.close()
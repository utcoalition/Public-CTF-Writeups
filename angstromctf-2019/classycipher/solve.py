def encrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e

for i in xrange(0, 256):
  ciphertext=':<M?TLH8<A:KFBG@V'
  flag = encrypt(ciphertext, i)
  if flag[:5] == 'actf{':
    print (i, flag)

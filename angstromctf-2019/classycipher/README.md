# Classy Cipher 

20 points  - 717 solves

```
Every CTF starts off with a Caesar cipher, but we're more classy.
```

## Solution

Source code was provided in the challenge, which looked like

```python
from secret import flag, shift

def encrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e

assert encrypt(flag, shift) == ':<M?TLH8<A:KFBG@V'
```

We are given a cipher-text and a knowledge about the logic which was used to encrypt the ciphertext. It is evident that the encrypt algorithm is XOR (Exclusive-OR). 

The modulus 0xff ensures what chr data point lies until 255. Now, our goal is to figure out the correct shift, as we know that chr would lie within 255. I can simply brute-force the values.

I quickly code a solver for it

```python
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
```

Hence, we retrieve

```
(39, 'actf{so_charming}')
```

#### Flag: actf{so_charming}

# Brainmeat 

75 points  - 91 solves

```
I am having a beef with someone that is so bad I cant even think! He sent me a message but I think he was having a stroke. Please decipher the message while I beat them up.
```


## Solution

We can notice here, that a lot of characters are present including alphanumeric and couple other special characters. The challenge name implies `Brainfuck` Esoteric language. 

The brainfuck character set contains `><+-.,[]` which we can see most of them present inside our ciphertext. We can write a regex to remove other non-brainfuck characters.

```
/[^A-Za-z0-9]/gm
```

This will match everything except `A-Za-z0-9` . The `g` denotes global and `m` being multi-line matches.

We get the output as

```
+[--------->++<]>+.++.-------.[--->+<]>+.[->+++++<]>-.-[--->+<]>--.+[->+++<]>+.++++++++.------------.[--->+<]>-.------------.---.[->+++<]>--.-[--->+<]>--.[--->+<]>----.+++[->+++<]>++.++++++++.+++++.[++>---<]>--.-[-->+++++++<]>.[->+++<]>.--[--->+<]>.+[->+++<]>+.++++++++.+++++.[->+++<]>++.++++.+++..+.>--[-->+++<]>.
```

Now, we can easily decode this encoded brainfuck text

#### Flag: sun{fuck_the-brain#we!got^beef}

# Linux RE-1

300 points - ?? solves

[Attachments](https://drive.google.com/open?id=14j2MtDjO3-szCrVFVI-UBJs-KEEv4MED)


## Solution

Idea is to simply patch the binary by nop'ing out `ptrace()` call - a lowkey anti debugging method. 

Next, it's trivial to put the breakpoint on compare function. I use `gef` as my debugger. 

The key was `1337key` and the data was retrieved from the register. 

```
>>> xor("\x50\x5d\x03\x43\x03\x56\x0b\x6e\x40\x02\x5a\x1b\x54\x1c\x6e\x4b\x03\x45\x34\x06\x0b\x05\x50\x58\x5a\x58","1337key")

'an0th3r_s1mp1e_x0r_cr4ckm3'
```

#### Flag: CodefestCTF{an0th3r_s1mp1e_x0r_cr4ckm3}

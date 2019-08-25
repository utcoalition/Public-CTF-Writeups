# Linux RE-2 

500 points - ?? solves

[Attachments](https://drive.google.com/open?id=1ni1WHmIkf_sm-N6oFn0BL0jwf7VPhEtB)


Solved by: knapstack

## Solution

Multiple ways to solve it - Manual static analysis by looking through the disassembly or just by using symbolic execution. 

Here was my retrieval. `char *` indices are below.

```
local_62 = 'l'
local_63 = 'o'
local_64 = 'o'
local_65 = 't'
local_66 = '_'
local_67 = 'e'
local_68 = 'm'
local_69 = 'o'
local_6a = 's'
local_6b = '_'
local_6c = 'd'
local_6d = 'e'
local_6e = 's'
local_6f = 'u'
local_70 = '_'
local_71 = 'e'
local_72 = 'v'
local_73 = 'd'
local_74 = 'l'
local_75 = 'u'
local_76 = 'o'
local_77 = 'h'
local_78 = 's'
```

#### Flag: CodefestCTF{shouldve_used_some_tool}
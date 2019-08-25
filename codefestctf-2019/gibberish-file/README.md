# Gibberish File

100 Points - ?? Solves

```
This file seems to have a weird encoding. Reverse it to find the flag.
```
[Attachments](
https://drive.google.com/open?id=1WWDSc0kGKghzCx0DitZdgViXzLpvpKQZ)

Solver: knapstack

## Solution

At first 

```
⇒  file output.txt
output.txt: Non-ISO extended-ASCII text, with very long lines, with no line terminators
```

It says `Non-ISO extended-ASCII text`, being said that one option is to brute all available encodings on the system. 

That sounds like a bit overkill. As the description, loosely gives out the approach which is to apparently reverse the content of the bytes.

```
$ python gibberish_solve.py

$ file not_gibberish
not_gibberish: UTF-8 Unicode text, with very long lines, with no line terminators
```

#### Flag: CodefestCTF{LiTErAL_REVERSinG}
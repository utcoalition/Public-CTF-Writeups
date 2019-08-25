# Windows RE

500 points - ?? Solves

```
You are given a Windows application which is a simple authentication app. Enter the correct password and get the flag.
```

[Attachment](https://drive.google.com/open?id=1ncmi3VVxzmnj0xFBoFlY5ysnFJGweJr3)

Solved by: knapstack

## Solution

Trivial authentication app. Booted up Windows VM. My initial recon and looking at resources - I knew that this was packed by ConfuserEx. It was a .NET binary - which make things easier on top of it.

I unpacked the binary, The app name was `verifier`. 

The password was discovered as `thisisa1337password`

which provides access to the flag

#### Flag: CodefestCTF{51mp13_1npu7_v411d4710n_8u7_w17h_4_7w157}
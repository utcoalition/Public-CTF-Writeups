# Image Corruption

100 points - ?? Solves

```
You are given a corrupted file. This file has the flag. Find it.
```

[Attachments](https://drive.google.com/open?id=1t5d_lKkdoG1aicBJYhM8wqh7Ispk0G4U)

Solver: knapstack
## Solution

Provided an image, which was broken. Inspecting it on byte level, I saw there are lot of instance of `matrix`. At some point, there are instances like `ma?rix` , `m??rix` , `m???ix`, etc. 


I had a lot of ideas on how to approach this problem. One of them was to simply xor the image file as binary with 'matrix' string.

```
$python solve.py
```

##### CodefestCTF{f1l35_h4v3_m461c_by735}
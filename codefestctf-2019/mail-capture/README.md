# Mail Capture

100 points - ??? Solves

```
Bob got hold of this file when going through the files of the email client on his old computer. Help him find the hidden message.
```

[Attachments](https://drive.google.com/open?id=1NBfs7sKYaFsylri3chrpmZdhkAIDD97y)

Solver: knapstack

## Solution

The file is a uuencoded text. 

```
$ file encoded_file
encoded_file: uuencoded or xxencoded text, ASCII text
```

From here, it's just plug and chug

https://www.dcode.fr/uu-encoding

```
[In]: E0V]D969E<W1#5$9[-V@Q-5\Q-5\T7V,P,#%?,VYC,&0Q;CE]"@``
`

[Out] CodefestCTF{7h15_15_4_c001_3nc0d1n9}
```

##### Flag: CodefestCTF{7h15_15_4_c001_3nc0d1n9}
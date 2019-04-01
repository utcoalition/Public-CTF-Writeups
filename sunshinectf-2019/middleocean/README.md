# Middle Ocean

75 points - 41 Solves

```
I made a deal with Hulch Hogan (Hulk Hogan's brother) for a treasure map can you get the treaure for me?
```


## Solution:

We were provided a file with the following content.

```
CMM72222+22
CQC52222+22
CH9J2222+22
9H9M2222+22
8PQ42222+22
9P4G2222+22
8Q572222+22
```

These are Plus-Codes, which is address for places which typically don't have one. It's a very minimal representation of addresses.

More information is available [here](https://plus.codes/). We can hover to the map section and apply each code one after the other.

Below is the translation of the Plus-Code to it's respective co-ordinates

```
CMM72222+22 : 83.000062,85.000063
CQC52222+22 : 78.000062,123.000063
CH9J2222+22 : 77.000062,52.000062
9H9M2222+22 : 57.000062,53.000062
8PQ42222+22 : 45.000062,102.000063
9P4G2222+22 : 52.000062,110.000063
8Q572222+22 : 33.000062,125.000063
```

We extract the numbers before the decimal point and retrieve the following

```
83 85 78 123 77 52 57 53 45 102 52 110 33 125
```

These are decimal (base-10) representation of ASCII letters. We can decode it using `chr()` and get

#### Flag: SUN{M495-f4n!}

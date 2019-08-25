# Cats are Awesome

200 Points - 1 Solve

```
This image has a flag hidden in it. Find it.
```

[Attachments](https://drive.google.com/open?id=1YtdrhvXBQHs-Z-C6qWbPdCdN4YOoSmMo)

Solver: knapstack

## Solution

I attempted this challenge as the final challenge to all-kill solves, because it had no prior solves. 

I downloaded the image, looked briefly into it.

First things first,

```
$ file cute_kittens.jpg
cute_kittens.png: PNG image data, 480 x 330, 8-bit/color RGB, non-interlaced
```

Interestingly enough, the file extension was `.jpg` but the contents were 

```
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
````

I tried to dump LSB, MSB and manually inspected image bytes. Nothing particular stood out.

Afterwards, I went to scout for visually similar image to the challenge provided.

```
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 480
Image Height                    : 330
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 480x330
Megapixels                      : 0.158
```

Following are the attributes, the file size of the image was 189kB. At this point, I found some images which were visually similar with same dimensions - although there were JPEG. All of them.

For instance, I downloaded 2 of the original images


```
⇒  ls | grep cute
cute_kittens.png
cute_kittens.zip
cute_kittens_original.jpg
cute_kittens_original1.jpg
```


Both of them were ~40Kb. The size of the file was roughly 4 times more than the original image. Also, the lack of availibility of the native png for the visually similar image was a big red flag for me. That being said, I knew that this is for sure a steganography challenge. More likely the ones which have embed data.

Now, I tried basic steganography tools over it. No success that way. There are a hell lot of tools, and finding the one which author used is not a simple task. 

I thought something smart by that point. I thought after downloading the jpg, the author ran some stego tool on it and it embed flag in original file and author forgot to change extension. The challenge being supplied with `.jpg` was a good indication.

The stego algorithm might have changed file data
But author might have done something like

```
$ ./tool -in original.jpg -out cute_kittens.jpg
```

Now, that I intuitively had figured out this plausible reason, I lowered down the complexity to search stegano tools. 

Within no time, I found [Stegify](https://github.com/DimitarPetrov/stegify), which had same stego generation mechanism which I anticipated.

Next, 

```
⇒  go run stegify.go -op decode -carrier cute_kittens.png -result solve.png
```

```
⇒  file solve.png
solve.png: Zip archive data, at least v?[0x30a] to extract
```

Then,

```
hexdump -C solve.png
00000000  50 4b 03 04 0a 03 00 00  00 00 99 84 0e 4f 78 26  |PK...........Ox&|
00000010  3b ec 10 00 00 00 10 00  00 00 11 00 00 00 69 73  |;.............is|
00000020  20 74 68 69 73 20 74 68  65 20 66 6c 61 67 3f 4e  | this the flag?N|
00000030  6f 70 65 2c 20 6e 6f 74  20 68 65 72 65 2e 0a 50  |ope, not here..P|
00000040  4b 01 02 3f 03 0a 03 00  00 00 00 99 84 0e 4f 78  |K..?..........Ox|
00000050  26 3b ec 10 00 00 00 10  00 00 00 11 00 00 00 00  |&;..............|
00000060  00 00 00 00 00 20 80 b4  81 00 00 00 00 69 73 20  |..... .......is |
00000070  74 68 69 73 20 74 68 65  20 66 6c 61 67 3f 50 4b  |this the flag?PK|
00000080  05 06 00 00 00 00 01 00  01 00 3f 00 00 00 3f 00  |..........?...?.|
00000090  00 00 00 00 43 6f 64 65  66 65 73 74 43 54 46 7b  |....CodefestCTF{|
000000a0  68 31 64 31 6e 67 5f 62  33 68 31 6e 64 5f 31 6e  |h1d1ng_b3h1nd_1n|
000000b0  6e 30 63 33 6e 74 5f 6b  31 74 74 33 6e 35 7d 0a  |n0c3nt_k1tt3n5}.|
000000c0
```

#### Flag: CodefestCTF{h1d1ng_b3h1nd_1nn0c3nt_k1tt3n5}

The overall time which took me to solve this challenge, was about 30 minutes. 300+ CTFs experience to the rescue. 😉
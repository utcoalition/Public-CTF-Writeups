# I Like It

40 points  - 605 solves

```
Now I like dollars, I like diamonds, I like ints, I like strings. Make Cardi like it please.

```

## Solution


The challenge gives us an executable. When run, it asks for a string. 
```
alice$ ./i_like_it 
I like the string that I'm thinking of: 
```
By running `strings` on it we can check for any interesting strings in the executable.
```
alice$ strings i_like_it 
/lib64/ld-linux-x86-64.so.2
libc.so.6
exit
__isoc99_sscanf
puts
__stack_chk_fail
stdin
printf
fgets
strlen
strcmp
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
%R	 
UH-p
AWAVA
AUATL
[]A\A]A^A_
I like the string that I'm thinking of: 
okrrrrrrr
Cardi don't like that.
I said I like it like that!
```

The line after `I like the string that I'm thinking of` stands out, using it we can get to the next stage.
```
I like the string that I'm thinking of: 
okrrrrrrr       
I said I like it like that!
I like two integers that I'm thinking of (space separated): 
```

Now we fire up `gdb` and take a look at what numbers where looking for. Typing disas main disassembles the main function which is the starting point of the executable.
```
gdb ./i_like_it 
(gdb) disas main
```
Which gives us
```
Dump of assembler code for function main:
   0x0000000000400850 <+170>:	lea    -0x34(%rbp),%rcx
   0x0000000000400854 <+174>:	lea    -0x38(%rbp),%rdx
   0x0000000000400858 <+178>:	lea    -0x30(%rbp),%rax
   0x000000000040085c <+182>:	mov    $0x400a1d,%esi
   0x0000000000400861 <+187>:	mov    %rax,%rdi
   0x0000000000400864 <+190>:	mov    $0x0,%eax
   0x0000000000400869 <+195>:	callq  0x400680 <__isoc99_sscanf@plt>
   0x000000000040086e <+200>:	mov    -0x38(%rbp),%edx
   0x0000000000400871 <+203>:	mov    -0x34(%rbp),%eax
   0x0000000000400874 <+206>:	add    %edx,%eax
   0x0000000000400876 <+208>:	cmp    $0x88,%eax
   0x000000000040087b <+213>:	jne    0x400897 <main+241>
   0x000000000040087d <+215>:	mov    -0x38(%rbp),%edx
   0x0000000000400880 <+218>:	mov    -0x34(%rbp),%eax
   0x0000000000400883 <+221>:	imul   %edx,%eax
   0x0000000000400886 <+224>:	cmp    $0xec7,%eax
   0x000000000040088b <+229>:	jne    0x400897 <main+241>
   0x000000000040088d <+231>:	mov    -0x38(%rbp),%edx
   0x0000000000400890 <+234>:	mov    -0x34(%rbp),%eax
   0x0000000000400893 <+237>:	cmp    %eax,%edx
   0x0000000000400895 <+239>:	jl     0x4008ab <main+261>
```
The lines after scanf tells us that were putting the read numbers into the registers %edx and %eax
```
   0x0000000000400869 <+195>:	callq  0x400680 <__isoc99_sscanf@plt>
   0x000000000040086e <+200>:	mov    -0x38(%rbp),%edx
   0x0000000000400871 <+203>:	mov    -0x34(%rbp),%eax
```

The first test done on the two numbers is if their sum equals 0x88 which is 136 in decimal. The jne jumps to the program exit so we know the two numbers must add up to 136.
```
   0x0000000000400874 <+206>:	add    %edx,%eax               adds the two numbers and puts the result into eax
   0x0000000000400876 <+208>:	cmp    $0x88,%eax              checks that the result is equal to 0x88
   0x000000000040087b <+213>:	jne    0x400897 <main+241>     jumps to the exit if they are not equal.
```

The second test done checks if the product of the two numbers is 0xe7 which is 3782 in decimal.
```
   0x000000000040087d <+215>:	mov    -0x38(%rbp),%edx         reads numbers of the stack into edx and eax
   0x0000000000400880 <+218>:	mov    -0x34(%rbp),%eax 
   0x0000000000400883 <+221>:	imul   %edx,%eax                multiplies the two numbers and puts the result into eax
   0x0000000000400886 <+224>:	cmp    $0xec7,%eax              checks the product is 3783 
   0x000000000040088b <+229>:	jne    0x400897 <main+241>      jumps to exit if not equal
```
The third test checks if the first number is less than the second number. 
```
   0x000000000040088d <+231>:	mov    -0x38(%rbp),%edx         reads number of stack into edx and eax
   0x0000000000400890 <+234>:	mov    -0x34(%rbp),%eax
   0x0000000000400893 <+237>:	cmp    %eax,%edx                
   0x0000000000400895 <+239>:	jl     0x4008ab <main+261>      checks that the first number is less than second number.
```
By solving the system of equations x+y = 136 and x*y = 3783 and x < y, we learn that x= 39 and y = 97. Which gives our flag.
```
alice$ ./i_like_it 
I like the string that I'm thinking of: 
okrrrrrrr
I said I like it like that!
I like two integers that I'm thinking of (space separated): 
39 97
I said I like it like that!
Flag: actf{okrrrrrrr_39_97}
```

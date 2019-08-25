import sys,os

for line in open(sys.argv[1], "r"):
    elem = line.split('+')
    for e in elem:
        p = e[0]
        n = int(e[2:])
        if p == "1":
            sys.stdout.write("X"*n)
        else:
            sys.stdout.write(" "*n)
    print

print done
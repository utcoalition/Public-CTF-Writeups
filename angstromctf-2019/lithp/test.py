def a(x,y):
    if not y:
        return 0
    else:
        return a(x, y -1 ) + x

def main():
    aa = a(2, 3)
    b = a(2, 4)
    c = a(2, 5)

    d = a(3, 2)
    e = a(4, 2)
    f = a(5, 2)

    print(aa)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

main()

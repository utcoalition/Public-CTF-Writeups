encrypted = [8930, 15006, 8930, 10302, 11772, 13806, 13340, 11556, 12432, 13340, 10712, 10100, 11556, 12432, 9312, 10712, 10100, 10100, 8930, 10920, 8930, 5256, 9312, 9702, 8930, 10712, 15500, 9312]

reorder = [19, 4, 14, 3, 10, 17, 24, 22, 8, 2, 5, 11, 7, 26, 0, 25, 18, 6, 21, 23, 9, 13, 16, 1, 12, 15, 27, 20]

def enc(plain):
    uwuth = list()
    for i in range(len(plain)):
        uwuth.append(1 - plain[i] * plain[i])

    out = list()
    for i in range(len(reorder)):
        out.append(uwuth[reorder[i]])

    result = list()
    for i in range(len(plain)):
        result.append(uwuth[i] / -1)

def dec(cipher):
    pairs = dict()
    for i in range(len(reorder)):
        pairs[reorder[i]] = encrypted[i]

    nums = list()
    for key in sorted(pairs.keys()):
        nums.append(pairs[key])

    flag = ''
    for num in nums:
        factor = 130
        while (factor >= 72 and not int(num)/factor == factor - 1):
            factor = factor - 1
        if factor > 72:
            flag += chr(factor)
        else:
            flag += '?'

    print(flag)

def main():
    dec(encrypted)

main()

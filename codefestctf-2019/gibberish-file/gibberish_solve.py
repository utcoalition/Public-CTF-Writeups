f = open('output.txt', 'rb')
xx = f.readlines()
buf2 = xx[0][::-1]
f1 = open('not_gibberish', 'wb')
f1.write(buf2)
f1.close()
f.close()
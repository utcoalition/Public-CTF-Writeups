import requests

f = open('solve.txt','w')
for i in xrange(0,1000):
        r = requests.get("http://34.212.86.199:9001/random-static-strings")
        f.write(r.text.encode('utf-8').strip())

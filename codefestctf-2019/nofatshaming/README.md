# No Fatshaming

600 points - ?? Solves

```
The admin is too lazy to login. Can you find the key for him? 

http://chall1.pythonanywhere.com/
```

Solved by: knapstack


## Solution

Interesting challenge, this is a web+re challenge. The reversing part is straightforward which is to reverse `challenge.js` 

The `cck` generation process was as below

```javascript
  function firstLoad(domLoad) {
        var sha256 = new jsSHA('SHA-256', 'TEXT');
        var please_hash_me = domLoad['id'] + '\x20000\x20114328\x20000\x20' + domLoad['time'];
        sha256.update(please_hash_me);
        var hashed = sha256.getHash("HEX");
        return hashed;
    }

```

There are lot of interesting stuff going on in the javascript.

 I debugged, static reversed for couple of minutes. (_Although, skipping the explaination part due to writeup time constraint._)

 Idea is to leak current session timestamp, forge it and login. and recursively try for all users.

```
$ python solve.py
```

#### Flag: CodefestCTF{1AmTeHHHAX00Rr4uj8rfi4e$%y5yhrf}
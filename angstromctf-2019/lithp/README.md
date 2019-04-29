# Lithp
## Misc, 60 points

### Prompt

My friend gave me this program but I couldn't understand what he was saying - what was he trying to tell me?

*Author: fireholder*

### Solution

We are given a file written in Lisp (oh boy) that we must decipher:

```lisp
;LITHP

(defparameter *encrypted* '(8930 15006 8930 10302 11772 13806 13340 11556 12432 13340 10712 10100 11556 12432 9312 10712 10100 10100 8930 10920 8930 5256 9312 9702 8930 10712 15500 9312))
(defparameter *flag* '(redacted))
(defparameter *reorder* '(19 4 14 3 10 17 24 22 8 2 5 11 7 26 0 25 18 6 21 23 9 13 16 1 12 15 27 20))

(defun enc (plain)
    (setf uwuth (multh plain))
    (setf uwuth (owo uwuth))
    (setf out nil)
    (dotimes (ind (length plain) out)
        (setq out (append out (list (/ (nth ind uwuth) -1))))))

(defun multh (plain)
    (cond
        ((null plain) nil)
        (t (cons (whats-this (- 1 (car plain)) (car plain)) (multh (cdr plain))))))

(defun owo (inpth)
    (setf out nil)
    (do ((redth *reorder* (cdr redth)))
        ((null redth) out)
        (setq out (append out (list (nth (car redth) inpth))))))

(defun whats-this (x y)
    (cond
        ((equal y 0) 0)
        (t (+ (whats-this x (- y 1)) x))))

;flag was encrypted with (enc *flag*) to give *encrypted*
```

After much Googling and documentation reading, I was able to annotate the file with some pseudocode that described what the program was doing:

```lisp
;LITHP

(defparameter *encrypted* '(8930 15006 8930 10302 11772 13806 13340 11556 12432 13340 10712 10100 11556 12432 9312 10712 10100 10100 8930 10920 8930 5256 9312 9702 8930 10712 15500 9312))
(defparameter *flag* '(redacted))
(defparameter *reorder* '(19 4 14 3 10 17 24 22 8 2 5 11 7 26 0 25 18 6 21 23 9 13 16 1 12 15 27 20))

(defun enc (plain) ; define funtion enc that takes in plain
    (setf uwuth (multh plain)) ; uwuth = multh(plain)
    (setf uwuth (owo uwuth)) ; uwuth = owo(uwuth)
    (setf out nil) ; out = list()
    (dotimes (ind (length plain) out) ; for i in range(len(plain))
        (setq out (append out (list (/ (nth ind uwuth) -1))))))
        ; out += list(uwuth[ind] / -1)

(defun multh (plain) ; def multh(plain)
    (cond
        ((null plain) nil) ; if plain == null: return list()
        (t (cons (whats-this (- 1 (car plain)) (car plain)) (multh (cdr plain))))))
        ; whats-this(1 - plain[0], plain[0]), multh (plain[1:])

(defun owo (inpth) ; def owo(inpth)
    (setf out nil) ; out = list()
    (do ((redth *reorder* (cdr redth))) ; loop through reorder, cutting off front element each time
        ((null redth) out) ; if redth == null: return out
        (setq out (append out (list (nth (car redth) inpth))))))
        ; out += list(inpth[redth[0]])

(defun whats-this (x y) ; def whats-this(x, y)
    (cond
        ((equal y 0) 0) ; if not y: return 0
        (t (+ (whats-this x (- y 1)) x)))) ; return whats-this(x, y-1) + x

;flag was encrypted with (enc *flag*) to give *encrypted*
```

I then translated this encoding function into a Python program:

```Python
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
```

To get the flag back, I just did all the encoding steps backwards to make a decoding function:

```Python
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
```

Run the program and you will get the flag: `actf{help_me_I_have_a_lithp}`

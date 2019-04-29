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

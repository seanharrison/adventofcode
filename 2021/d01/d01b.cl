; Count the number of increases in the input file. 
; - Open input file as a stream 
; - Read it one line at a time. 
; - Even if the file is 3TB, this method will still work.

(defparameter filepath (or (cadr *posix-argv*) "input"))
(defparameter previous nil)
(defparameter increases 0)
(defparameter stack ())

(with-open-file (input filepath :direction :input)
  (loop for line = (read-line input nil)
        while line
        do (setq stack (cons (parse-integer line) stack))
           (if (>= (length stack) 3)
               (progn
                (setq stack `(
                    ,(car stack)
                    ,(cadr stack)
                    ,(caddr stack)))
                (let ((value (reduce '+ stack)))
                  (if (and previous (> value previous))
                      (incf increases))
                  (setq previous value))))))

(print `(:increases ,increases))

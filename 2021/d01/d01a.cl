; Count the number of increases in the input file. 
; - Open input file as a stream 
; - Read it one line at a time. 
; - Even if the file is 3TB, this method will still work.

(let ((filepath (or (cadr *posix-argv*) "input"))
      (increases 0)
      (previous nil))
  (with-open-file (input filepath :direction :input)
    (loop for line = (read-line input nil)
          while line
          do (let ((value (parse-integer line)))
               (if (and previous (> value previous))
                   (incf increases))
               (setf previous value))))

  (print `(:increases ,increases)))

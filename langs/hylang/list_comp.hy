(for [i (range 10)]
  (print i))

(print
  (sum
    (lfor
      i (range 10)
      :if (= (% i 2) 0)
      ((fn [x] (* x x)) i))))

(defn factorial [n]
  (if (<= n 1)
    1
    (* n (factorial (- n 1)))))

(defmain [&rest args]
  (for [n (cut args 1)]
    (setv fmt "Factorial of {} is {}.")
    (print (fmt.format n (factorial (int n))))))

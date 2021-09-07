#!/usr/bin/env hy
(print (sum (map int (list (str (** 2 1000))))))

(defn maps [xs func] (map func xs))
(->
    (** 2 1000)
    str
    list
    (maps int)
    ; NOTE putting lambda here did not work (fn [xs] (map int xs))
    sum
    print
)

(-> (** 2 1000) str list (maps int) sum print)

(print
  (sum
    (lfor
       c (str (** 2 1000))
       (int c))))

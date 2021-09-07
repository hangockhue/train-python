#!/usr/bin/env hy

(-> (lfor
       num (range 1000)
       :if (or (= (% num 3) 0)
               (= (% num 5) 0)
           )
       num
    )
    sum
    print
)

(import requests)

(defn split-comma [x] (x.split ","))
(defn httpbin [slug]
  (setv r (requests.get "https://httpbin.org/ip"))
  (print "Your IP is" :end ": ")
  (print (->
           (get (r.json) "origin")
           split-comma
           first)))

(defmain [&rest args]
  (setv slug (second args))
  (if (= slug "ip")
    (httpbin slug)
    (print "require arg: ip")))

open Printf

let rec fizzbuzz n =
  if n == 0 then
    []
  else if n mod 15 == 0 then
    "FizzBuzz" :: fizzbuzz (n - 1)
  else if n mod 3 == 0 then
    "Fizz" :: fizzbuzz (n - 1)
  else if n mod 5 == 0 then
    "Buzz" :: fizzbuzz (n - 1)
  else string_of_int n :: fizzbuzz (n - 1)

let () =
  List.iter (printf "%s ") (fizzbuzz 100 |> List.rev)

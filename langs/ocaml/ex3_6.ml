open Printf

let () =
    let n = 1
    and months_days = [("Jan", 31); ("Feb", 28); ("Mar", 31)]
    in let month, days = List.nth months_days (n-1)
    in printf "%s %d\n" month days

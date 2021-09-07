open Printf

let rec aux n = match n with
| 0 ->
        ["0 = 5 * 0"]
| n ->
        (sprintf "%d = 5 * %d" n (n/5)) :: (aux (n - 5))

let make_list n = List.rev (aux n)

let () =
    List.iter (printf "%s\n") (make_list 100)

open Printf

type 'a btree = Empty | Node of 'a * 'a btree * 'a btree

let rec member x btree =
    match btree with
    Empty -> false
    | Node(y, left, right) ->
            if x = y then true else
                if x < y then member x left else member x right


let rec insert x btree =
    match btree with
    Empty -> Node(x, Empty, Empty)
    | Node(y, left, right) ->
            if x <= y then Node(y, insert x left, right) else Node(y, left, insert x right)

let () =
    printf "%b\n" (member 3 (insert 2 Empty));
    printf "%b\n" (member 3 (insert 2 (insert 3 Empty)));;

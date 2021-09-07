(*
a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

*)
open Printf

let rec range a b =
    let rec helper i k r =
        if i < k then helper (i+1) k (i :: r)
        else r
        in
    List.rev (helper a b [])

let prd outer inner inner2 =
    List.concat (List.concat (
        List.map (fun i ->
            List.map (fun j ->
                List.map (fun k -> (i,j,k)) inner2) inner) outer))
                |> List.filter (fun (a,b,c) -> b == (10-a) * c)

let () =
    List.iter (fun (a,b,c) -> printf "(%d,%d,%d)" a b c) (
        prd (range 1 10) (range 1 10) (range 1 10)
    )

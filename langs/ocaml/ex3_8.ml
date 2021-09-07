open Printf

let reverse_str s =
    let rec str_to_list s = match s with
    | "" ->
            []
    | s ->
            (String.make 1 (String.get s 0)) :: (str_to_list (String.sub s 1 ((String.length s) - 1)))
    in (str_to_list s) |> List.rev |> String.concat ""


let is_palindrome s = match String.length(s) with
| 0 ->
        false
| 1 ->
        false
| n ->
        let clean s =
            s |> String.lowercase_ascii |> String.split_on_char ' ' |> String.concat "" in
        String.equal (clean s) (reverse_str (clean s))

let () =
    let s = "Ci vi c" in
    if is_palindrome s then
        printf "%s is palindrome" s
    else
        printf "%s is NOT palindrome" s

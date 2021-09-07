open Printf



let () =
  let data = ["I"; "Love"; "You"; "Chiu"; "Chiu"] in
  let result = List.mapi(fun index elem -> (index, elem)) data
  in List.iter (fun (idx, elem) -> printf "%d: %s\n" idx elem) result

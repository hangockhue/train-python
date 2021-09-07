let rec binary n =
  if n == 0 then ""
  else binary (n / 2) ^ (string_of_int (n mod 2));;

let solve data =
  (* String from the last number 1 in binary of data *)
  let bin = binary data in
  let idx = (String.rindex bin '1') in
  String.sub bin idx (String.length bin - idx)


let () =
  let d = 1000 in
  Printf.printf "%8s\n" (solve d);


open Printf

let remove_ext filename =
  let last_dot = String.rindex filename '.' in
  String.sub filename 0 last_dot

let () =
  let test =  "....slsslslsls...sls" in
  printf "%s" (remove_ext test)

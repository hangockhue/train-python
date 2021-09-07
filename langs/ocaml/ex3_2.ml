open Printf
let data = "
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
"

let () =
  let first_chars = data
              |> String.trim
              |> String.split_on_char '\n'
              |> List.map (function s -> String.make 1 (String.get s 0))
  in
  let result =  ((String.concat "" first_chars) |> String.lowercase_ascii |> String.capitalize_ascii)
  in printf "%s\n" result

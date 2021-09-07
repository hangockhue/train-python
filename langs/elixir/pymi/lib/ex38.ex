defmodule Ex38 do
  def solve(string) do
    normalized = string |> String.replace(" ", "") |> String.downcase()

    if String.length(normalized) < 3 do
      false
    else
      normalized == String.reverse(normalized)
    end
  end
end

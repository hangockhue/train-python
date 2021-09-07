defmodule Ex354 do
  @doc """
  Creates a string which contains N random ASCII letters.
  """
  def solve(n) do
    ascii_letter = Enum.concat(Enum.map(?a..?z, & &1), Enum.map(?A..?Z, & &1))

    Stream.repeatedly(fn -> Enum.random(ascii_letter) end)
    |> Enum.take(n)

    # |> IO.inspect
  end
end

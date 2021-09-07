defmodule Ex358 do
  @doc """
    '''Create a list which contains N lists,
    each list contains N numbers from 0->N-1.

    E.g with N = 10:

    matrix = [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      ...
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    Then returns a string looks like below

      0********0
      *1******1*
      **2****2**
      ***3**3***
      ****44****
      ****55****
      ***6**6***
      **7****7**
      *8******8*
      9********9
  """
  def solve() do
    solve(10)
  end

  defp solve(n) do
    Stream.repeatedly(fn -> List.duplicate("*", n) end)
    |> Enum.take(n)
    |> make([], 0)
    |> Enum.map(fn line -> Enum.join(line, "") end)
    |> Enum.join("\n")
  end

  defp make([], out, _) do
    out |> Enum.reverse()
  end

  defp make([h | t], out, count) do
    make(
      t,
      [
        List.replace_at(h, count, Integer.to_string(count))
        |> List.replace_at(9 - count, Integer.to_string(count))
      ] ++ out,
      count + 1
    )
  end
end

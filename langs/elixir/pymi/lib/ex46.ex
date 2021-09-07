defmodule Ex46 do
  @doc """
    Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]
  """
  def solve("") do
    []
  end

  def solve(text) do
    do_solve(text, [], [])
  end

  defp do_solve("", auxilary, result) do
    if auxilary != [] do
      Enum.reverse([convert_aux_to_number(auxilary) | result])
    else
      Enum.reverse(result)
    end
  end

  defp do_solve(text, auxilary, result) do
    head = String.at(text, 0)
    tail = String.slice(text, 1..-1)

    case Integer.parse(head) do
      {val, _} ->
        do_solve(tail, [val | auxilary], result)

      :error ->
        if auxilary == [] do
          do_solve(tail, auxilary, result)
        else
          number = convert_aux_to_number(auxilary)
          do_solve(tail, [], [number | result])
        end
    end
  end

  defp convert_aux_to_number(aux) do
    aux |> Enum.reverse() |> Enum.map(&to_string/1) |> Enum.join("") |> String.to_integer()
  end
end

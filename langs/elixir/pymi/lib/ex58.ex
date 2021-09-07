defmodule Ex58 do
  @doc """
    Trả về biểu diễn của 20 mã ASCII từ 33 đến 53 theo format
    [(33, BIEUDIENCUA33), ...]
    Unicode codepoint của các số từ 0->9, a-z, A-Z.
    Unicode codepoint tương ứng với ký tự ``\t`` ``\n``, `` ``
  """
  def format_code_repr(n) do
    {n, [n]}
  end

  def solve() do
    ascii_ = 33..52 |> Enum.map(fn i -> format_code_repr(i) end)
    # binary pattern matching
    <<tab::utf8>> = "\t"
    <<newline::utf8>> = "\n"
    <<space::utf8>> = " "
    # TODO alphanumeric = [Enum.map(0..9
    todo = []
    {ascii_, todo, tab, newline, space}
  end
end

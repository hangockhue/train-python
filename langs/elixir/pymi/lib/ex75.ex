defmodule Ex75 do
  @doc """
  Return tuple chứa
  - Đường dẫn tới code của module `os` -> does not apply here as Elixir is compiled
  - list chứa các attribute của os và sys
  - Số dòng trong module `os` -> does not apply as no source
  """
  def solve(module) do
    # https://hexdocs.pm/elixir/Module.html#c:__info__/1
    length(apply(module, :module_info, [:exports]))
  end
end

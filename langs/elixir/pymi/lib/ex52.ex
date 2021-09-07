defmodule Ex52 do
  @data [
    %{
      name: "Hoang",
      phone: "0988888888",
      languages: ["Python", "C", "SQL", "HTML", "CSS", "JavaScript", "Golang"]
    },
    %{name: "Duy", girl_friend: "Maria"},
    %{name: "Dai", girl_friend: "Angela"},
    %{name: "Tu"}
  ]
  @doc """
    Trả về list thông tin các học viên sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các học viên đều học được các ngôn ngữ lập trình
    trong "languages" của học viên "Hoang".
    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.
    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia thay bạn gái, không còn bạn gái nữa.
  """
  def update(student, hoang_old_langs) do
    case student[:name] do
      "Hoang" ->
        Map.update(student, :languages, "", fn langs -> langs ++ ["Elixir"] end)

      "Tu" ->
        Map.update(student, :girl_friend, "Do Anh", fn _ -> "Do Anh" end)
        |> Map.put(:languages, hoang_old_langs)

      "Duy" ->
        Map.delete(student, :girl_friend) |> Map.put(:languages, hoang_old_langs)

      _ ->
        student |> Map.put(:languages, hoang_old_langs)
    end
  end

  def solve() do
    students = @data
    # NOTE: use string as key would return nil
    # Note that keywords are always atoms, even when quoted
    hoang_old_langs = Enum.find(students, fn h -> h[:name] == "Hoang" end)[:languages]
    students |> Enum.map(fn student -> update(student, hoang_old_langs) end)
  end
end

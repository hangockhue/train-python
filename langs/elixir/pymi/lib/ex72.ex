defmodule Weapon do
  defstruct [:name, :damage]
end

defmodule Fighter do
  defstruct [:name, :hp, :weapon]

  def attack(attacker, opponent) do
    {attacker,
     %Fighter{
       name: opponent.name,
       hp: opponent.hp - attacker.weapon.damage,
       weapon: opponent.weapon
     }}
  end
end

defmodule Ex72 do
  @doc """
  Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
  máu (int), vũ khí.
  Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
  khi đánh trúng.
  Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
  thắng.
  """
  def solve() do
    gun = %Weapon{name: "gun", damage: 100}
    sword = %Weapon{name: "sword", damage: 20}
    p1 = %Fighter{name: "P1", hp: 100, weapon: gun}
    p2 = %Fighter{name: "P2", hp: 100, weapon: sword}
    # random here
    if :random.uniform() > 0.5 do
      IO.puts("P1 #{p1.name} play first")
      play(p1, p2)
    else
      IO.puts("P2 #{p2.name} play first")
      play(p2, p1)
    end
  end

  defp play(p1, p2) do
    IO.puts(
      "#{p1.name}:#{p1.hp} used #{p1.weapon.name}:#{p1.weapon.damage} attacks #{p2.name}:#{p2.hp} has #{
        p2.weapon.name
      }:#{p2.weapon.damage}"
    )

    {p1, p2} = Fighter.attack(p1, p2)

    if p2.hp <= 0 do
      IO.puts("#{p2.name} dies")
      p1
    else
      play(p2, p1)
    end
  end
end

# https://projecteuler.net/problem=54
from collections import namedtuple
from enum import Enum, auto


class Suit(Enum):
    """
    Enum dùng để tạo kiểu dữ liệu mới cho một tập hữu hạn các giá trị,
    ví dụ: các size quần áo, các chất trong bộ bài, ...
    Trong bài này nó tương đương với dùng các string C S H D nhưng
    sẽ có exception nếu đầu vào đưa một giá trị khác.

    Nếu không dùng Enum, có thể thêm dòng kiểm tra sau trước khi tạo card:

    if s not in 'CSHD':
        raise ValueError("Bad suit: {}".format(s))
    """

    C = auto()
    S = auto()
    H = auto()
    D = auto()


# namedtuple giống tuple, nhưng cho phép truy cập giá trị
# c.value and c.suit, cũng có thể viết 1 class tương ứng.
Card = namedtuple("Card", ["value", "suit"])


def new_card(s):
    v, s = s
    if v == "T":
        v = 10
    elif v == "J":
        v = 11
    elif v == "Q":
        v = 12
    elif v == "K":
        v = 13
    elif v == "A":
        v = 14
    return Card(int(v), Suit[s])


def parse_hand(hand):
    if isinstance(hand, str):
        cards = hand.split()
    else:
        cards = hand

    return sorted([new_card(i) for i in cards], key=lambda x: x.value)


#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
def values(hand):
    return [i.value for i in hand]


def high_card(hand):
    return max(values(hand))


def is_one_pair(hand):
    vs = values(hand)
    return [vs.count(i) for i in set(vs)].count(2) == 1 and [
        i for i in vs if vs.count(i) == 2
    ].pop()


def is_two_pairs(hand):
    vs = values(hand)
    return [vs.count(i) for i in set(vs)].count(2) == 2 and [
        i for i in vs if vs.count(i) == 2
    ]


def is_three_of_a_kind(hand):
    vs = values(hand)
    return [vs.count(i) for i in set(vs)].count(3) == 1 and [
        i for i in vs if vs.count(i) == 3
    ].pop()


def is_straight(hand):
    vs = values(hand)
    return [i - vs[0] for i in vs] == [0, 1, 2, 3, 4] and vs


def is_flush(hand):
    return len(set([i.suit for i in hand])) == 1 and values(hand).pop()


def is_full_house(hand):
    t = is_three_of_a_kind(hand)
    p = is_one_pair(hand)
    if t and p:
        return [t, p]
    else:
        return False


def is_four_of_a_kind(hand):
    vs = values(hand)
    return {vs.count(i) for i in set(vs)} == {1, 4} and [
        i for i in vs if vs.count(i) == 4
    ].pop()


def is_straight_flush(hand):
    s = is_straight(hand)
    f = is_flush(hand)
    if s and f:
        return [s, f]
    else:
        return False


def is_royal_flush(hand):
    return (
        is_flush(hand)
        and values(hand) == [10, 11, 12, 13, 14]
        and values(hand)
    )


ranks = [
    is_royal_flush,
    is_straight_flush,
    is_four_of_a_kind,
    is_full_house,
    is_flush,
    is_straight,
    is_three_of_a_kind,
    is_two_pairs,
    is_one_pair,
]


def find_winner(h1, h2):
    hand1 = parse_hand(h1)
    hand2 = parse_hand(h2)
    assert len(hand1) == 5
    assert len(hand2) == 5
    winner = 0
    print("checking", h1, h2)
    for check in ranks:
        r1 = check(hand1)
        r2 = check(hand2)
        if r1 and r2:
            print("handle tie")
            if r1 > r2:
                print("1 win", hand1, hand2)
                winner = 1
            elif r2 > r1:
                winner = 2
                print("2 win", hand1, hand2)
            else:
                assert r1 == r2
                if high_card(hand1) > high_card(hand2):
                    winner = 1
                    print("1 win")
                else:
                    winner = 2
                    print("2 win")

            break
        elif r1:
            print("1 win")
            winner = 1
            print(r1, check.__name__)
            break
        elif r2:
            print("2 win")
            winner = 2
            print(r2, check.__name__)
            break
    if winner == 0:
        if high_card(hand1) > high_card(hand2):
            winner = 1
            print("1 win highcard", high_card(hand1))
        else:
            winner = 2
            print("2 win highcard", high_card(hand2))

    assert winner != 0
    return winner


print(is_one_pair(parse_hand("2D 2H")))
print(is_two_pairs(parse_hand("2D 4H 2H 4D")))


h1 = "5H 5C 6S 7S KD"
h2 = "2C 3S 8S 8D TD"
find_winner(h1, h2)

h1 = "2D 9C AS AH AC"
h2 = "3D 6D 7D TD QD"
find_winner(h1, h2)


with open("p054_poker.txt") as f:
    games = f.readlines()


cntr = 0
for g in games:
    cards = g.strip().split()

    h1, h2 = cards[:5], cards[5:]

    cntr = cntr + 1 if find_winner(h1, h2) == 1 else cntr

print(cntr)

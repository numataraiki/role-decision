# スートと数字を定義
suits = ["S", "C", "D", "H"]
numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#ストレート確認用の配列
hnumber=[]

# 入力される手札
hoc = []

# 各役を判定する関数を定義する
#フラッシュを判定する
def is_flush(hand):
    return len(set(suit for suit, rank in hand)) == 1

#ストレートを判定する
def is_straight(hand):
    rank_indices = hnumber
    # 1から13までのストレート判定
    if rank_indices == list(range(rank_indices[0], rank_indices[0] + 5)):
        return True
    # KからAにまたがって連続している場合の判定
    if rank_indices == [1, 2, 3, 12,13]:
        return True
    elif rank_indices == [1, 2, 3, 4, 13]:
        return True
    elif rank_indices == [2, 3, 11, 12, 13]:
        return True
    
    return False

#ロイヤルフラッシュを判定する
def is_royal_straight_flush(hand):
    return is_flush(hand) and set(rank for suit, rank in hand) == {"A", "K", "Q", "J", "10"}

#ストレートフラッシュの判定。ストレートとフラッシュを呼び出して判定
def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)

#手札をスートと数字に分けてそれぞれの数を返す。フルハウスやフォーカードの判定に使用する
def classify_by_rank(hand):
    rank_counts = {}
    for suit, rank in hand:
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    return sorted(rank_counts.values(), reverse=True)


#役を判定するための関数。ロイヤルフラッシュから役が強い順に呼び出す。
def hand_rank(hand):
    if is_royal_straight_flush(hand):
        return "ロイヤルストレートフラッシュ"
    elif is_straight_flush(hand):
        return "ストレートフラッシュ"
    elif classify_by_rank(hand) == [4, 1]:
        return "フォーカード"
    elif classify_by_rank(hand) == [3, 2]:
        return "フルハウス"
    elif is_flush(hand):
        return "フラッシュ"
    elif is_straight(hand):
        return "ストレート"
    elif classify_by_rank(hand) == [3, 1, 1]:
        return "スリーカード"
    elif classify_by_rank(hand) == [2, 2, 1]:
        return "ツーペア"
    elif classify_by_rank(hand) == [2, 1, 1, 1]:
        return "ワンペア"
    else:
        return "ハイカード"


# カードを入力させ、各配列に格納、ストレート確認用配列をソートしておく
print("「スート 数字」の形式で各カードの情報を入力")
for i in range(5):
    print(str(i + 1) + "つ目のカード")
    row_input = input()
    suit, number = map(int, row_input.split())
    hoc.append((suits[suit], numbers[number - 1]))
    hnumber.append(number)
    hnumber.sort()
#ユーザーが入力した手札を表示する
result = ' '.join([''.join(sublist) for sublist in hoc])
print(result)

#呼び出しと役の表示
rank = hand_rank(hoc)
print("役: " + rank)
print()


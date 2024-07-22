"""タプル構造の基本的な操作を行うプログラム
タプルは、リストと似ているが、
データの変更ができない
中身を変更されたくない時に使う
"""

# タプルにミュータブルオブジェクトを入れた場合
# 中身は変更できる
t = ([1, 2, 3], [4, 5, 6])
t[0][0] = 100
print(t)

t = ({"v1": 1, "v2": 2}, {"v3": 3})
t[0]["v1"] = 10
print(t)

# ()を省略してもtupleを定義できる
t = 1, 2, 3
print(f"{t}___{type(t)}")

# tupleの結合
# extendはできないが新しいtupleを作ると結合可能
# 1つだけのtupleを作るには、 ,を最後につける
tuple_1 = (1, 2, 3)
tuple_2 = (4,)
join_tuple = tuple_1 + tuple_2
print(join_tuple)

# アンパッキング
# tupleの中身を変改して入れる
num_tuple = (10, 20)
x, y = num_tuple
print(f"x{x}__y{y}")

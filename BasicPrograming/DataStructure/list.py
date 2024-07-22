"""リスト構造の基本的な操作を行うプログラム"""

# pythonでlistを表すには、[]を使う
sample_list = [1, 2, 3, 4, 5]
print(sample_list)

# リストには、index番号がついている
# index番号は、0から始まる
print(f"index0_{sample_list[0]}")  # 1


# 最後の要素を出力したい時は、-1を使う
print(f"last_{sample_list[-1]}")  # 5

# 1~3番を抜き出したい時は[:]を使う
s = sample_list[0:3]
print(s)


# 一つ飛ばしで実行する場合
# [1,3,5]
s = sample_list[::2]
print(s)

# 後から表示する時は？
# [5,4,3,2,1]
s = sample_list[::-1]
print(s)

# listの要素数を知る時は？
list_length = len(sample_list)
print(list_length)

# リストをネストさせるには？
list_1 = [1, 2, 3]
list_2 = [3, 2, 1]

list_3 = [list_1, list_2]
print(list_3)

# リスト3から1を取り出すには？
ans_1 = list_3[0][0]
ans_2 = list_3[1][2]
print(print(f"{ans_1}_{ans_2}"))


# 特定のインデックス範囲を指定して入れ替える
list = [1 for _ in range(4)]
list[1:4] = [2, 3, 4, 5]
print(list)

# index3を消す時は？
n = [1, 2, 3, 4, 5]
del n[2]
print(n)

# 最初に見つけた2を削除する
n = [1, 2, 2, 2, 3]
n.remove(2)
print(n)


# 2つのlistを1つのlistにする
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9]
join_list = list_1 + list_2
print(join_list)

# xを拡張してyと結合
x = [1, 2, 3, 4]
y = [5, 6, 7, 8, 9]
x.extend(y)
print(x)

# 3が格納されているindexは？
list_3 = [1, 2, 3, 4, 5, 6]
target_index = list_3.index(3)
print(target_index)

# 指定した位置以降から3を探す
r = [1, 2, 3, 4, 5, 1, 2, 3, 3]
print(r.index(3))
print(r.index(3, 8))

# 3が含まれる個数を求める
r = [1, 2, 3, 4, 5, 1, 2, 3, 3]
print(r.count(3))

# 逆順ソート
r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r.sort(reverse=True)
print(r)

# 通常ソート
r.sort()
print(r)

# 文字列をスペースで区切って、配列に入れる
s = "Hello world !!!"
s_l = s.split(" ")
print(s_l)

j_l = " ".join(s_l)
print(j_l)


# 値渡しと参照渡し
i = [1, 2, 3, 4, 5]

# 下記の場合は、iが格納されているポインタの位置をjに渡している
# よって参照後に値を変えると元のデータの値も変わる
j = i
j[0] = 100
print(id(j))
print(id(i))

# 文字列型などで同様のことをしてもおこらない
a = 111111
b = a
b = 222222
print(id(a))
print(id(b))

# これはミュータブルなオブジェクトのみ変更されてる

dict_1 = {"value1": 1, "value2": 2}
dict_2 = dict_1
print(id(dict_1))
print(id(dict_2))

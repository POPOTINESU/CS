"""辞書構造の基本的な操作を行うプログラム
keyとvalueで表されるデータ構造
"""

# dictの宣言
# 呼び出しはkeyを指定する
d = {"x": 1, "y": 2}
print(d)
print(d["x"])
print(d["y"])

# xに代入
d["x"] = 10
print(d["x"])

# keyの一覧を取得する
print(d.keys())
# valueの一覧を取得する
print(d.values())

d2 = {"x": 10, "y": 11, "z": 100}
d.update(d2)
print(d)

# getメソッドを使うと参照先がなくてもエラーが起こらない
# Noneと返ってくる
print(d.get("value3"))

# 　popかdelで削除ができる
d.pop("z")
print(d)

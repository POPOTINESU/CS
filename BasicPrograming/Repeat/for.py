# 10ずつ増やしてループ
for i in range(0, 101, 10):
    print(i)

# indexも取り出す
for i, fruit in enumerate(["apple", "banana", "orange"]):
    print(i, fruit)


# zip関数
# これで簡単にまとめてループを回すことができる

days = ["M", "T", "W"]
fruits = ["T", "N", "A"]
drinks = ["coffee", "tea", "grape"]

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# 辞書で取得する方法
# items()を使うことでkeyもvalueも取得することができる
# items()の中に、tuple型として入って、アンパッキングされる

d = {"x": 100, "y": 200}

for k, v in d.items():
    print(k, ":", v)

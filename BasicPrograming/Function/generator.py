"""ジェネレーター
forなどと似ているが、
要素を取り出す毎に,要素を生成している

処理数が多くなった時に、通常のforだと応答しなくなる可能性がある
yieldを使って処理を小分けにすると処理の負担を軽くすることができる
"""


def greeting():
    yield "Good morning"
    yield "afternoon"
    yield "night"


for g in greeting():
    print(g)

g = greeting()
print(next(g))
print("KOKI")
print(next(g))
print("SHIGEKUNI")

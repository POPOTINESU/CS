# 引数が省略された時
# =""でデフォルト引数を決めておくことができる
# 検索時とあったら楽かも？

# ただし、デフォルト引数をリストや辞書で使うと参照渡しになる
# その場合はデフォルト引数を指定すべきではない


def abc(a="a", b="b", c="c"):
    print(a)
    print(b)
    print(c)


abc("ab", "fnoew")

# 引数が多い場合は、*argsを使う


def say_something(*args):
    for arg in args:
        print(arg)


say_something("fnoew", "nofgew", "nonofe")

t = ("bofe", "ofew")
# *tupleでアンパッキングして引数を渡せる
say_something("nofew", *t)


def say_dict(**kwargs):
    # 辞書型の場合は、**kwargsで定義できる
    for key, value in kwargs.items():
        print(f"{key}:{value}")


say_dict(entree="beef", drink="coffee")


dict_set = {"key": 124, "key2": 344}
say_dict(**dict_set)

"""例外処理

try:
    試みる内容
except:
    エラーが発生した場合
"""

l_1 = [1, 2, 3]
i = 5

try:
    l_1[i]
except IndexError as ex:
    # 存在しないindex番号にアクセスすると例外処理を行う
    print(f"Don't worry{ex}")


l_2 = [1, 2, 3]
i = 5
del l_2
try:
    l_2[i]
except IndexError as ex:
    # 存在しないindex番号にアクセスすると例外処理を行う
    print(f"Don't worry{ex}")
except NameError as ne:
    print(f"名前エラー{ne}")

# Exceptionとも書くことはできるがこの書き方は推奨されない
# 全てのエラーを取得することができるが、先の処理を進めるのに、
# よくわからないエラーが出ても先に進めないようにするべき


# 最後に必ず実行する処理

l_2 = [1, 2, 3]
i = 5
del l_2
try:
    l_2[i]
except IndexError as ex:
    # 存在しないindex番号にアクセスすると例外処理を行う
    print(f"Don't worry{ex}")
except NameError as ne:
    print(f"名前エラー{ne}")
else:
    # エラーが発生しない場合は、elseが実行される
    print("例外が発生しなかった")
finally:
    # 真偽に関わらず実行される
    print("clean up")


class UppercaseError(Exception):
    # Exceptionを継承したクラスで条件を書くと
    # カスタムの例外を発生させることができる
    pass


def check():
    words = ["APPLE", "orange", "banana"]
    for word in words:
        if word.isupper():
            # 独自の例外を呼び出すことができる
            raise UppercaseError(word)


check()

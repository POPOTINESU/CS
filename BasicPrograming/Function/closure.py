"""クロージャー
関数内に宣言する関数のこと

outerを参照して呼び出した時に、
戻り値としてinner関数自体が返る
返ってきたオブジェクトをさらに呼び出すとinner関数を実行できる
"""


def outer(a, b):
    def plus():
        return a + b

    return plus


f = outer(1, 2)
r = f()
print(r)


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.14159)


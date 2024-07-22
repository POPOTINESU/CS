"""while
"""

count = 0
while count <= 100:
    if count == 99:
        count += 1
        # ここから下はスキップできる
        continue
    elif count == 98:
        count += 1
        # breakでwhile自体を抜ける
        # ここでループを出た場合は、elseも実行されない
        break

    print(count)
    count += 1
else:
    # whileはTrueの間継続してループする
    # ループを抜けるとFalseになるからelseが実行される
    count = 1000
    print(count)

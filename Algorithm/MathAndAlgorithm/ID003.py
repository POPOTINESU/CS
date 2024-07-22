# 整数NとN個のAが与えられる
# それらの足し算

N = int(input())


def sum_of_integers(*args):
    result = 0
    for number in args:
        result += number
    return result


print(sum_of_integers(*tuple(map(int, input().split()))))

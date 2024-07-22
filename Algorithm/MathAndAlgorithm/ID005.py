# N個の整数の和を割った数

N = int(input())

nums = tuple(map(int, input().split()))


def modulo(nums):
    sum_num = 0
    for num in nums:
        sum_num += num
    modulo = sum_num % 100
    return modulo


print(modulo(nums))

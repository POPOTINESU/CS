def add_num(a, b):
    return a + b


print("start")
r = add_num(10, 20)
print("end")

print(r)


def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return wrapper


def add_nums(a, b):
    return a + b


f = print_info(add_nums)
r = f(10, 20)
print(r)


@print_info
def diff_num(a, b):
    return a - b


r = diff_num(2, 1)
print(diff_num)

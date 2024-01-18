# decorator
def description(f):  # closure
    def inner(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args)
        return r

    return inner


def squares(n):
    """
    제곱 함수
    """
    return n * n

@description
def power(b, e):
    """
    거듭제곱 함수
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result


f1 = description(squares)
print(f1(9))
print(power(2, 10))
# f2 = description(power)
# print(f2(2, 10))

# print(squares(7))
# print(squares.__doc__)

# def my_range(first=0, last=5, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# r = my_range()
# print(r, type(r))
#
# for x in r:
#     print(x)
# for x in r:
#     print(x)
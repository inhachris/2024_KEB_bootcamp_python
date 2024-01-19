def factorial_repetition(n) -> int:
    """
    반복문을 이용한 팩토리얼 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def factorial_recursion(n):
    """
    재귀함수를 사용한 팩토리얼 함수
    :param n: 정수, int
    :return: function, int
    """
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

# print(factorial_repetition(int(input("number : "))))
# print(factorial_recursion(int(input("number : "))))
number = int(input("number : "))
print(factorial_repetition(number))
print(factorial_recursion(number))
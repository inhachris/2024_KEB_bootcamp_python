def get_odds(n) -> int:
    """
    1부터 n까지의 홀수를 발생시키는 제네레이터
    :param n: int
    :return: int
    """
    for i in range(1, n+1, 2):
        yield i

cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt += 1
    if cnt == 3:
        print(f'Third number is {odd}')
        break

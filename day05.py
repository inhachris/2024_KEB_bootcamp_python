# Assignment Exercise 9.2 (p.242)

def get_odds():
    for number in range(1, 10, 2):
        yield number

# print(list(get_odds()))

i = 0
for odd in get_odds():
    i += 1
    if i == 3:
        print("세 번째 홀수:", odd)
        break

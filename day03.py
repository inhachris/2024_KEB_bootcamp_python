# prime number
number = int(input("Input number : "))
cnt = 0
i = 2

while i < number:
    if number % i == 0:
        cnt = cnt + 1
        break
    # print(i, end=' ')
    i = i + 1

if cnt == 0:
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number!')







# subjects = {'python': 'kim', 'c++': 'sung', 'data structure': 'kim', 'database': 'kang'}
# print("{0[python]} {0[database]}".format(subjects))
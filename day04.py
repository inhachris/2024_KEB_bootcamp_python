# squares = list()
# squares.append(1*1)
# squares.append(2*2)
# squares.append(3*3)
# squares.append(4*4)
# squares.append(5*5)
# print(squares)

# squares = list()
# for i in range(1, 6, 1):
#     squares.append(i*i)
# print(squares)

# list comprehension
# squares = [i*i for i in range(1, 6, 1)]
# print(squares)

even_squares = [i*i for i in range(1, 6, 1) if i % 2 == 0]
print(even_squares)
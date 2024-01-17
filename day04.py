t1 = (5)
t2 = 5,    # , 반드시 있어야 함
t3 = (5, )
t4 = (5, 7)
t5 = 5, 7
print(type(t1), type(t2), type(t3), type(t4), type(t5))
t6 = "python", "kim"    # packing
print(type(t6), t6[1])
subject, prof = t6    # unpacking
# a, b, c = t6    # ValueError: not enough values to unpack (expected 3, got 2)
print(prof)
print(subject)
t7 = ()
t8 = tuple()
print(type(t7), type(t8), type(9,), type((9,)))
t9 = 1, 2, 3
t10 = 1, 2
print(t9 == t10)
print(t9 <= t10)
print(t9 > t10)
t11 = 4.43,
t12 = 3.97, 4.1, 3.27
#print(t11 + t12)
print(id(t11))
t11 = t11 + t12    # t11 += t12
print(id(t11))
print(t11)
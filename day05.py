# Assignment Exercise 9.4 (p.242)

class OopsException(Exception):
    pass

# raise OopsException()

try:
    raise OopsException("Oops!")
except OopsException:
    print('Caught an oops')

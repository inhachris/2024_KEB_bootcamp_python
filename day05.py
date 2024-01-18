# Assignment Exercise 9.2 (p.242)

def test(func):
    def new_function(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return new_function

@test
def example_function():
    print("This is the main function.")

example_function()

def desc(f):
    def wrapper():
        print("study")
        f()
    # print("a")
    return wrapper

def something():
    print("do something")

s = desc(something)
s()
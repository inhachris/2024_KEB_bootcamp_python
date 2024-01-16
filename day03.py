# assignment Exercise 6.2 (p.143)

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("oops")
        break
    number = number + 1
# prime number
numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        continue  #pass
    else:
        i = 2
        while i*i < number:  # performance issue
            if number % i == 0:
                is_prime = False
                break
            i = i + 1
            #print(i, end=' ')  # loop count
        if is_prime:
            pass
            print(number, end=' ')
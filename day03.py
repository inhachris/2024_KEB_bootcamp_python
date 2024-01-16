# prime number
numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')
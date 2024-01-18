# prime number with function
def isprime(n) -> bool:
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

while True:
    menu = input("1) Fahrenheit -> Celsius     2) Celsius -> Fahrenheit \
    3) Deciding Prime Number     4) Prime Numbers In a Section     5) Quit Program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}°F   ->   Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}°C\n')

    elif menu == '2':
        celsius = float(input('Input Celcius : '))
        print(f'Celsius : {celsius}°C   ->   Fahrenheit : {((celsius*9.0/5.0) + 32.0):.4f}°F\n')

    elif menu == '3':
        number = int(input("Input number : "))
        if isprime(number):
            print(f'{number} is prime number\n')
        else:
            print(f'{number} is NOT prime number\n')

    elif menu == '4':
        n1, n2 = map(int, input("Input first second number : ").split())
        n1, n2 = min(n1, n2), max(n1, n2)

        # numbers = input("Input first second number : ").split()
        # n1 = int(numbers[0])
        # n2 = int(numbers[1])
        # if n1 > n2:
        #     n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end=' ')
        print("\n")

    elif menu == '5':
        print("Terminate Program")
        break
# (100°F - 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F

while True:
    menu = input("1) Fahrenheit -> Celsius     2) Celsius -> Fahrenheit     \
    3) Deciding Prime Number     4) Prime Numbers In a Section     5) Quit Program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}°F   ->   Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}°C\n')

    elif menu == '2':
        celsius = float(input('Input Celcius : '))
        print(f'Celsius : {celsius}°C   ->   Fahrenheit : {((celsius*9.0/5.0) + 32.0):.4f}°F\n')

    elif menu == '3':
        number = int(input("Input number : "))
        is_prime = True

        if number < 2:
            print(f'{number} is NOT prime number!\n')
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f'{number} is prime number\n')
            else:
                print(f'{number} is NOT prime number!\n')

    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                pass
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime: print(number, end=' ')

        print("\n")

    elif menu == '5':
        print("Terminate Program")
        break

    else:
        print("Invalid Menu!\n")
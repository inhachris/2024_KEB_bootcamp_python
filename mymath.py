
def isprime(n) -> bool:
    """
    A function that returns as a boolean whether the number passed as a parameter is a prime number.
    :param n: Parameter to judge
    :return: True if prime number, False if not prime number.
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


def fahrenheit_to_celsius(fahrenheit) -> float:
    """
    Function to convert Fahrenheit temperature to Celsius temperature
    :param fahrenheit:
    :return: celsius temperature
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0


def celsius_to_fahrenheit(celsius) -> float:
    """
    Function to convert Celsius temperature to Fahrenheit temperature
    :param celsius:
    :return: fahrenheit temperature
    """
    return (celsius*9.0/5.0)+32.0



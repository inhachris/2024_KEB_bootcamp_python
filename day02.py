# (100°F - 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F

menu = input("1) Fahrenheit -> Celsius     2) Celsius -> Fahrenheit     3) Quit Program : ")

if menu == '1':
    fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}°F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}°C')
elif menu == '2':
    celsius = float(input('Input Celcius : '))
    print(f'Celsius : {celsius}°C, Fahrenheit : {((celsius*9.0/5.0) + 32.0):.4f}°F')
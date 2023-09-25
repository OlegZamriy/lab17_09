number1 = float(input("Введіть перше число: "))

number2 = float(input("Введіть друге число: "))

if number1 < number2:
    min_number = number1
else:
    min_number = number2

print(f"Мінімальне число: {min_number}")

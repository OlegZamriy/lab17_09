number1 = float(input("Введіть перше число: "))

number2 = float(input("Введіть друге число: "))

operation = input("Виберіть операцію (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
    print(f"Сума: {result}")
elif operation == "-":
    result = number1 - number2
    print(f"Різниця: {result}")
elif operation == "*":
    result = number1 * number2
    print(f"Добуток: {result}")
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
        print(f"Частка: {result}")
    else:
        print("Помилка: Ділення на нуль неможливе")
else:
    print("Помилка: Невідома операція")

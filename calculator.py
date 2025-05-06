def menu():
    print("""
Выберите действие:
1. Ввести A
2. Ввести B
3. Выполнить операцию "+"
4. Выполнить операцию "-"
5. Выполнить операцию "*"
6. Выполнить операцию "/"
0. Выход
""")

# Новая функция для этой ветки:
def input_a():
    return float(input("Введите число A: "))

#Новая функция для этой ветки:
def input_b():
    return float(input("Введите число B: "))

# Новая функция для этой ветки
def add(a, b):
    return a + b

# Новая функция для этой ветки:
def subtract(a, b):
    return a - b

# Новая функция для этой ветки:
def multiply(a, b):
    return a * b

# Новая функция для этой ветки:
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

if __name__ == "__main__":
    a, b = None, None  # Инициализация переменных

    while True:
        menu()
        choice = input("Ваш выбор: ")  # Ждём ввода пользователя

        if choice == "0":
            print("Выход из программы.")
            break

        elif choice == "1":
            a = input_a()

        elif choice == "2":
            b = input_b()

        elif choice in ("3", "4", "5", "6"):
            if a is None or b is None:
                print("Ошибка: сначала введите A и B!")
                continue

            if choice == "3":
                print(f"Результат: {add(a, b)}")
            elif choice == "4":
                print(f"Результат: {subtract(a, b)}")
            elif choice == "5":
                print(f"Результат: {multiply(a, b)}")
            elif choice == "6":
                print(f"Результат: {divide(a, b)}")

        else:
            print("Неверный ввод! Попробуйте снова.")

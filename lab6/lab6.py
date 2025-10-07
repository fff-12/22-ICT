from deco import retry_on_none

@retry_on_none
def divide(a, b):
    if b == 0:
        print("Ділення на нуль неможливе.")
        return None
    return a / b

def main():
    try:
        a = float(input("Введіть чисельник (a): "))
        b = float(input("Введіть знаменник (b): "))
        result = divide(a, b)
        print(f"Результат ділення: {result}")
    except ValueError:
        print("Будь ласка, введіть дійсні числа.")

if __name__ == "__main__":
    main()

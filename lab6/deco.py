# Потійчук Максим – декоратор для автоматичного повторного виклику функції з новими аргументами, якщо вона повернула None.

def retry_on_none(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        while result is None:
            a = float(input("Введіть чисельник (a): "))
            b = float(input("Введіть знаменник (b): "))
            resultd = func(a, b)
            if resultd is not None:
                result = resultd
        return result
    return wrapper


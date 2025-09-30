# Потійчук Максим – декоратор для автоматичного повторного виклику функції з новими аргументами, якщо вона повернула None.

def retry_on_none(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            print("Повернення None, введіть нові аргументи.")
        return result
    return wrapper
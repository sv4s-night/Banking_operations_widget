from functools import wraps


def log(*, filename=None):
    """Декоратор логирования, регистрирующий детали выполнения функций"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper

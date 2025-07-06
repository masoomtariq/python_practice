# Defining the decorator
def decorator(func):

    def wrapper(a, b):

        if a < b:
            a, b = b, a
        return func(a, b)
    return wrapper

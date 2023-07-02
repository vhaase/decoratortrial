from Tools.demo.beer import n


def repeat(i):
    def decorator(func):
        def wrapper():
            for _ in range(i):
                func()

        return wrapper

    return decorator


@repeat(n)
def greet():
    print("Hallo")


input(n)
greet()

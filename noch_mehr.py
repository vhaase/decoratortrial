def my_decorator(func):
    def wrapper(a):
        print("Vor der Funktion")
        if type(a) == str:
            func(a)
        print("Nach der Funktion")

    return wrapper


def check(func):
    def wrapper(x: int):
        if func(x) > 100:
            return func(12)
        else:
            return func(x)
    return wrapper

@my_decorator
def my_function(x):
    print(f"Die Funktion wurde {x} ausgeführt")


@check
def calc(v):
    return v+88

my_function("soeben")

print(calc(9))

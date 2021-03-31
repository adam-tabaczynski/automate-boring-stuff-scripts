from functools import wraps

def my_deco(func):
    @wraps(func) # line here fixes issue with decorator. It gives to wrapper function properties of passed function (here, foo)
    def wrapper(*args, **kwargs):
        print("Function name: " + wrapper.__name__)
        print("Number of arguments: " + str(len(args) + len(kwargs)))
        res = func(*args, **kwargs)
        return res
    return wrapper

@my_deco
def foo(arg1, arg2, arg3): # these two lines equal to foo = my_deco(foo)
    print('')

foo(42, 44)

import functools

SETTINGS = 'settings'

def once(func):
    res = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if SETTINGS not in res:
            res[SETTINGS] = func(*args, **kwargs)
        return res[SETTINGS]
    return wrapper


@once
def initialize_settings():
    print("Settings initialized.")
    return {"token": 42}

print(initialize_settings())
print(initialize_settings())


def trace_if(condition):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                args_str = ', '.join(map(str, args)) + (', ' if args and kwargs else '') + "{" + ', '.join(f'{k}={v}' for k, v in kwargs.items()) + "}"
                print(f"{func.__name__}, {args_str}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
            

@trace_if(lambda x, y, **kwargs: kwargs.get("integral"))
def div(x, y, integral=False):
    return x // y if integral else x / y

print(div(4, 2))
print(div(4, 2, integral=True))



def n_times(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@n_times(3)
def do_something():
    print("Something is going on!")

do_something()
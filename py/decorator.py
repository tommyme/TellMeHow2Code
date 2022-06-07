import functools

def before(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(f'before {f.__name__}():')
        return f(*args, **kwargs)
    return wrapper

def print_x_before(x):
    print(x)
    return before


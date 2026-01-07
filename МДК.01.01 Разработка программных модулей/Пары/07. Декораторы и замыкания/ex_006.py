import time

def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} выполнялась {end_time - start_time:.3f} сек')
        return result
    return inner

@timer
def work():
    for _ in range(100000):
        pass
work()
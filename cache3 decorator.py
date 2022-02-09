from functools import wraps


def cache3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.count == 0:
            wrapper.cache = func(*args, **kwargs)
        wrapper.count = (wrapper.count + 1) % 3
        return wrapper.cache

    wrapper.cache = None
    wrapper.count = 0
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1

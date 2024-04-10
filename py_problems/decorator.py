import time


def time_with_format(format_str: str):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            start_time = time.time()
            retval = func(*args, **kwargs)
            print(
                f"{func.__name__} took: ", format_str.format(time.time() - start_time)
            )
            return retval

        return wrapped

    return wrapper


@time_with_format("{:.2f}s")
def plus(a, b):
    return a + b


@time_with_format("{:,.0f}s")
def wait(secs: int):
    time.sleep(secs)


plus(1, 2)
wait(1)


def another_wait(secs: int):
    time.sleep(secs)


wrapped_wait = time_with_format("{:,.3f}s")(another_wait)
wrapped_wait(2)

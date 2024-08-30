import functools
import datetime


def activate(mode):
    def log_function(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if mode == 1:
                res = func(*args, **kwargs)
                with open("C:/Users/andre/Desktop/log.txt", "a") as file:
                    file.write(
                        f"Function: {func.__name__} \n"
                        f"Arguments: {args}{kwargs} \n"
                        f"Result: {res} \n"
                        f"Timestamp: {datetime.datetime.now()} \n\n")
                return res
            else:
                print("Error")

        return wrapper

    return log_function


@activate(mode=1)
def calc_add(a, b):
    return a + b


calc_add(2, 3)

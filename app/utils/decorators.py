import functools
import asyncio



loop = asyncio.get_event_loop()

def with_executor(func):
    def wrapper(*args, **kwargs):
        partial = functools.partial(func, *args, **kwargs)
        return loop.run_in_executor(None, partial)

    return wrapper

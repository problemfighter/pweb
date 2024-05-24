import functools
import gc
import datetime
from datetime import timedelta
from functools import lru_cache, wraps


class PWebCache:
    enableCache: bool = True
    time1Minute = 60
    time30Minute = 60 * 30
    time1Hour = 60 * 60
    time1Day = 60 * 60 * 24
    time1Month = 60 * 60 * 24 * 30
    time1Year = 60 * 60 * 24 * 364

    @staticmethod
    def clean_all():
        gc.collect()
        objects = [i for i in gc.get_objects() if isinstance(i, functools._lru_cache_wrapper)]
        if objects:
            for cache_object in objects:
                cache_object.cache_clear()


def pweb_cache(maxsize: int = 128, expire_seconds: int = None, typed=False):
    def wrapper_cache(func):
        if PWebCache.enableCache:
            func = lru_cache(maxsize=maxsize, typed=typed)(func)

        if expire_seconds:
            func.lifetime = timedelta(seconds=expire_seconds)
            func.expiration = datetime.datetime.now(datetime.UTC) + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if func.expiration and datetime.datetime.now(datetime.UTC) >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.datetime.now(datetime.UTC) + func.lifetime

            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache

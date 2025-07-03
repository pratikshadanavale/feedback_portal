
import datetime
from functools import wraps

def log_access(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print(f"[{datetime.datetime.now()}] View accessed: {view_func.__name__}")
        return view_func(request, *args, **kwargs)
    return wrapper
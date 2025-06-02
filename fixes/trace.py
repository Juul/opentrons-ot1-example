from functools import wraps
import inspect


def traceable(*args):
    def _traceable(f):
        @wraps(f)
        def decorated(*call_args, **call_kwargs):
            res = f(*call_args, **call_kwargs)
            broker = EventBroker.get_instance()

            sig = inspect.signature(f)
            bound_args = sig.bind(*call_args, **call_kwargs)
            bound_args.apply_defaults()

            # Convert BoundArguments to a regular dict
            args_dict = dict(bound_args.arguments)

            broker.notify({
                'name': name,
                'function': f.__qualname__,
                'arguments': args_dict,
                'result': res
            })
            return res

        return decorated

    if len(args) == 1 and callable(args[0]):
        f = args[0]
        nonlocal_name = f.__qualname__
        return _traceable(f)
    else:
        nonlocal_name = args[0]
        name = nonlocal_name
        return _traceable


class EventBroker(object):
    _instance = None

    def __init__(self):
        self.listeners = []

    def add(self, f):
        self.listeners.append(f)

    def remove(self, f):
        self.listeners.remove(f)

    def notify(self, arguments):
        for listener in self.listeners:
            listener(arguments)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = EventBroker()
        return cls._instance

class TailCallable:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

class tailrec:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        x = self.f(*args, **kwargs)

        while isinstance(x, TailCallable):
            x = x.f()

        return x

    def tailcall(self, *args, **kwargs):
        return TailCallable(lambda: self.f(*args, **kwargs))

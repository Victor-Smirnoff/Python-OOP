class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, request, *args, **kwargs):
        if "method" not in request:
            return f'GET: {self.func(request)}'
        elif request["method"] != "GET":
            return None
        elif request["method"] == "GET":
            return f'{request["method"]}: {self.func(request)}'

    def __call__(self, request, *args, **kwargs):
        return self.get(request)

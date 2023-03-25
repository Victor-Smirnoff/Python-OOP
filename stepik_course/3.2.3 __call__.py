class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        for arg in args:
            x = '.' + arg.split('.')[-1]
            for extension in self.extensions:
                if x.endswith('.' + extension):
                    return True

        return False

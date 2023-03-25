class DigitRetrieve:
    def __call__(self, item, *args, **kwargs):
        return int(item) if item.isdigit() or item[1:].isdigit() else None

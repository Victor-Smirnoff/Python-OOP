class InputDigits:
    def __call__(self, func, *args, **kwargs):
        return list(map(int, func().split()))


input_dg = InputDigits()
res = input_dg(input)

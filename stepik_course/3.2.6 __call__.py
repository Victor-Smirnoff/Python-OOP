class RenderList:
    def __init__(self, type_list):
        if type_list == 'ul':
            self.type_list = type_list
        elif type_list == 'ol':
            self.type_list = type_list
        else:
            self.type_list = 'ul'

    def __call__(self, lst, *args, **kwargs):
        return ''.join([f'<{self.type_list}>\n'] + [f'<li>{x}</li>\n' for x in lst] + [f'</{self.type_list}>'])

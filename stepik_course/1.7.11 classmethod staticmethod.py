class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        if msg in cls.messages:
            cls.messages.remove(msg)

    @classmethod
    def set_like(cls, msg):
        cls.messages[cls.messages.index(msg)].fl_like = not cls.messages[cls.messages.index(msg)].fl_like

    @classmethod
    def show_last_message(cls, num):
        print(cls.messages[-num:])

    @classmethod
    def total_messages(cls):
        return len(cls.messages)

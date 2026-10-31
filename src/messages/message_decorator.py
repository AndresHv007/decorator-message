from .message import Message


class MessageDecorator(Message):
    def __init__(self, message: Message):
        self.message = message

    def render(self) -> str:
        return self.message.render()

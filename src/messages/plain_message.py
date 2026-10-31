from .message import Message
class PlainMessage(Message):
    def __init__(self, text: str): self.text=text
    def render(self): return self.text

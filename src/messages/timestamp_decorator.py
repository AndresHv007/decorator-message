from datetime import datetime

from .message import Message
from .message_decorator import MessageDecorator


class TimestampDecorator(MessageDecorator):
    def __init__(self, message: Message, timestamp: datetime):
        super().__init__(message)
        self.timestamp = timestamp

    def render(self) -> str:
        return f"[{self.timestamp:%Y-%m-%d %H:%M:%S}] {super().render()}"

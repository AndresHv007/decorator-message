from .message_decorator import MessageDecorator


class UrgentDecorator(MessageDecorator):
    def render(self) -> str:
        return f"[URGENT] {super().render()}"

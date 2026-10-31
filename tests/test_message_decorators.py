from datetime import datetime

from messages.plain_message import PlainMessage
from messages.timestamp_decorator import TimestampDecorator
from messages.urgent_decorator import UrgentDecorator


def test_decorators_stack_and_order_changes_prefixes():
    message = PlainMessage("Deploy complete")
    timestamp = datetime(2026, 10, 30, 12, 0, 0)

    urgent_first = UrgentDecorator(TimestampDecorator(message, timestamp))
    timestamp_first = TimestampDecorator(UrgentDecorator(message), timestamp)

    assert urgent_first.render() == "[URGENT] [2026-10-30 12:00:00] Deploy complete"
    assert timestamp_first.render() == "[2026-10-30 12:00:00] [URGENT] Deploy complete"
    assert message.render() == "Deploy complete"

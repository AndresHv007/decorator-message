from messages.plain_message import PlainMessage
def test_plain_message():
    assert PlainMessage("Deploy complete").render()=="Deploy complete"

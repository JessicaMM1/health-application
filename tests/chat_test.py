# Device module tests
import os, sys

# getting the name of the directory where this file is present.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from chat_api import create_message
from devices import status_code


def test_invalid_message_type():
    status = status_code()
    create_message("Mary", "sticker", "Hello World", status)

    assert status.error == ['Invalid message type']


def test_invalid_recipient_type():
    status = status_code()
    create_message(1234, "text", "hello", status)

    assert status.error == ['Invalid recipient type']


def test_json_output():
    status2 = status_code()
    out = create_message("Jake", "text", "Goodbye", status2)

    assert isinstance(out,str)

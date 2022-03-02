# Chat module

import json
from datetime import datetime 
import uuid

# from devices import status_code


valid_types = ["text", "image", "video", "audio"]


def create_message(recipient, type, content, status):

    if not isinstance(recipient,str):
        status.message = "Invalid recipient type"
        return
    
    if type not in valid_types:
        status.message = "Invalid message type"
        return
    
    if not isinstance(content, str):
        status.message = "Invalid content type"
        return

    # verify url
    # message id
    # add timestamp
    # convert to json

    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    unique_id = str(uuid.uuid4())
    
    new_message = {
        "messageID": unique_id[:8],
        "sender": "bob",
        "recipient": recipient,
        "date": date,
        "time": time,
        "message_type": type
        }

    if type == "text":
        new_message["body"] = content
 
    elif type in valid_types and type != "text":
        new_message["url"] = content
    
    out = json.dumps(new_message, indent=4)

    return out 


# status = status_code()
# out = create_message("mary", "text", "Hello world!", status)
# print(out)
# print(type(out))

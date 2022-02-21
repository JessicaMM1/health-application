# Test API - web app

import requests

BASE = "http://127.0.0.1:5000/"

put_device_info = {
                    "name": "t13343", 
                    "type": "thermometer", 
                    "serial_number": 6789,
                    "data": 32332,
                    "unit": "lbs"
                    }

# response = requests.get(BASE + "a1b2c3/device1.json")
response = requests.put(BASE + "a1b2c3/device9.json", put_device_info)
# print(type(response)) # requests.model.Response
print(response.json())

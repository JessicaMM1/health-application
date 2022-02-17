# Device interface skeleton - Celsius and Farenheit
import json
from datetime import datetime

now = datetime.now()

keys = [
        "A1B2C3",
        "a1b2c3",
        "Z9Y8X7",
        "z9x8y7"
        ]

# devices = (
#             "thermometer", 
#             "bp_monitor", 
#             "w_scale", 
#             "glucose_meter", 
#             "oximeter"
#             )

valid_devices = {
            "thermometer": ("C", "F"), 
            "bp_monitor": ("mmHg", "bpm"), 
            "w_scale": ("kgs", "lbs"), 
            "glucose_meter": "mg/dL", 
            "oximeter": ("SP02", "bpm"),
            }

# deviceInfo = {
#                 "name": str, *
#                 "type": str, *     Enum: [thermometer, bp_monitor, w_scale, glucose_meter, oximeter]
#                 "id": int,
#                 "measurement": [int], 
#                 "unit": str, *
#                 "time_stamp": str
#               }


class status_code:
    def __init__(self) -> None:
        self.success = True 
        self.error = []


class deviceInfo:

    ''' def __init__(self, *args) -> None:  # type, name, unit (optional)
        self.type = args[0]
        self.name = args[1]
        self.serialNumber = None
        self.measurement = None
    '''

    # >> Should device check be here?

    '''        
        # Check for unit scale (for now is just thermometer C/F)
        if len(args) == 3 and isinstance(args[2], str):
            # if args[2] == "C" or args[2] == "F":
            self.unit = args[2]
        else:
            self.unit = None
    '''

    def __init__(self, name, type, serial_number, measurement, unit) -> None:
        self.name = name
        self.type = type
        self.serial_number = serial_number
        self.measurement = measurement
        self.unit = unit


    # type = ""
    # name = ""
    # serialNumber = None
    # measurement = None

    # Manual input


    '''
        def set_measurements(self, measurement):
        self.measurement = measurement
        self.measurementsTime = now.strftime("%d/%m/%Y %H:%M:%S")
    '''

    def set_time(self):
        self.time_stamp = now.strftime("%d/%m/%Y %H:%M:%S")


def check_range(device):
    # Error codes:
    # 0 - no data

    print(">> check_range ", device.type, device.unit, device.measurement)

    if device.measurement is None:
        return False
    elif device.type == "thermometer":
        if device.unit == "C" and device.measurement >= 45:
            return False
        elif device.unit == "F" and device.measurement >= 108.14:
            return False

    return True


def read_data(key, device, status):

    # Add JSON as input

    print("input: ", type(device), device)

    # Convert (deserialize) JSON to dictionary & convert to deviceInfo object:
    if type(device) is str:
        try:
            with open(device, "r") as read_file:
                data = json.load(read_file)     # dict type
            # print(type(data)) 
            print(data)
            device = deviceInfo(**data)
            device.set_time()
            print(device.__dict__)

        except FileNotFoundError as e:
            status.success = False
            status.error.append(e.strerror)
            return 

        # print(type(device))
        # >>> check json validity

    elif type(device) is not deviceInfo:
        status.success = False
        status.error.append("Invalid input")
        return
    

    # check key (hardcoded list for now)
    print(">> key ", key, keys)

    if key not in keys:
        status.success = False
        status.error.append("Invalid key")

    valid_device = valid_devices.get(device.type)    # returns device's units 
    # print(valid_device)

    # check device type
    if valid_device is None:
        status.success = False
        status.error.append("Invalid device type")

    # check correct units for device
    if valid_device is not None and device.unit not in valid_device:
        print("in check")
        status.success = False
        status.error.append("Invalid units for device")

    # check measurements range
    if not check_range(device):
        status.success = False
        status.error.append("Invalid measurements")

    # Return JSON with timestamp 
    # Create (serialize) JSON from deviceInfo object:
    out_json = json.dumps(device.__dict__, indent=4)
    # print(encode)
    # print(type(encode))
    return out_json


print("----- main ------")

# t = deviceInfo("t1", "thermometer", None, 38, "C")
# print(t.type, t.name, t.unit)

# t.set_measurements(111)
# print(t.measurement)
# print(t.measurementsTime)

status = status_code()
out = read_data("a1b2c3", "device1.json", status)
print(status.success, status.error)
print(out)

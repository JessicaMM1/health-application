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

valid_devices = {
            "thermometer": ("C", "F"), 
            "bp_monitor": ("mmHg", "bpm"), 
            "w_scale": ("kgs", "lbs"), 
            "glucose_meter": "mg/dL", 
            "oximeter": ("SP02", "bpm"),
            }

# deviceInfo = {
#                 "name": str, 
#                 "type": str, *     Enum: [thermometer, bp_monitor, w_scale, glucose_meter, oximeter]
#                 "serial_number: int,
#                 "data": [int], 
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

    def __init__(self, name, type, serial_number, data, unit) -> None:
        self.name = name
        self.type = type
        self.serial_number = serial_number
        self.data = data
        self.unit = unit

    '''
        def set_measurements(self, measurement):
        self.measurement = measurement
        self.measurementsTime = now.strftime("%d/%m/%Y %H:%M:%S")
    '''

    def set_time(self):
        self.time_stamp = now.strftime("%d/%m/%Y %H:%M:%S")


def check_range(device):
    # Checks ranges according to device and unit
    print(">> check_range ", device.type, device.unit, device.data)

    if device.data is None or type(device.data) is not int:
        print("one")
        return False
    elif device.type == "thermometer":
        if device.unit == "C" and not 0 <= device.data <= 45:
            print("two")
            return False
        elif device.unit == "F" and not 32 <= device.data <= 108.14:
            return False

    return True


# def is_json_valid(data, status):
#     # Checks validity of file -> if dictionary contains all the required fields

#     # type
#     if "type" not in data:
#         status.success = False
#         status.error.append("No device type found")

#     # unit
#     if "unit" not in data:
#         status.success = False
#         status.error.append("No unit found")

#     # data
#     if "data" not in data:
#         status.success = False
#         status.error.append("No data found")

#     return status.success 


def read_data(key, device, status):

    # Add JSON as input
    print("input: ", type(device), device)

    # Convert (deserialize) JSON to dictionary & convert to deviceInfo object:
    if type(device) is str:
        try:
            with open(device, "r") as read_file:
                data = json.load(read_file)     # dict type
            # print(type(data)) 
            # print(data)

            # if not is_json_valid(data, status):
            #     # print("not valid")
            #     return
                device = deviceInfo(**data)
        
        except FileNotFoundError as e:
            status.success = False
            status.error.append(e.strerror)
            return 
        
        except TypeError:
            status.error.append("Missing JSON parameter")
            return

        # print(type(device))
    '''
        elif type(device) is not deviceInfo:
        status.success = False
        status.error.append("Invalid input")
        return
    '''

    if key not in keys:
        status.success = False
        status.error.append("Invalid key")

    valid_device = valid_devices.get(device.type)    # returns device's units 
    print(valid_device)

    # check device type
    if valid_device is None:
        status.success = False
        status.error.append("Invalid device type")

    # check correct units for device
    if valid_device is not None and device.unit not in valid_device:
        status.success = False
        status.error.append("Invalid units for device")

    # check measurements range
    if not check_range(device):
        status.success = False
        status.error.append("Invalid measurements")

    device.set_time()
    # Return JSON with timestamp 
    # Create (serialize) JSON from deviceInfo object:
    # out_json = json.dumps(device.__dict__, indent=4)
    # print(device.__dict__)
    # print(out_json)

    # print(encode)
    # print(type(encode))
    return device.__dict__


def add_data(key, device_dict, file, status):
    # 1. create device obj with given information
    print("ADD DATA ",  device_dict, type(device_dict))
    print(device_dict["name"])
    device = deviceInfo(**device_dict)
    print(device.type)
    

    # 2. verify information

    if key not in keys:
        status.success = False
        status.error.append("Invalid key")

    valid_device = valid_devices.get(device.type)    # returns device's units 
    print(valid_device)

    # check device type
    if valid_device is None:
        status.success = False
        status.error.append("Invalid device type")

    # check correct units for device
    if valid_device is not None and device.unit not in valid_device:
        status.success = False
        status.error.append("Invalid units for device")

    # check measurements range
    if not check_range(device):
        status.success = False
        status.error.append("Invalid measurements")

    device.set_time()

    # 3. write to given filename as JSON
    if status.success:
        with open(file, "w") as write_file:
            json.dump(device.__dict__, write_file, indent=4)     # dict type



# print("----- main ------")

# t = deviceInfo("t1", "thermometer", None, 38, "C")
# # print(t.type, t.name, t.unit)

# # t.set_measurements(111)
# # print(t.measurement)
# # print(t.measurementsTime)

# status = status_code()
# out = read_data("a1b2c3", "device123.json", status)
# print(status.success, status.error)
# print(out)

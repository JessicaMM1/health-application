# Device interface skeleton - Celsius and Farenheit
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

devices = {
            "thermometer": ("C", "F"), 
            "bp_monitor": ("mmHg", "bpm"), 
            "w_scale": ("kgs", "lbs"), 
            "glucose_meter": "mg/dL", 
            "oximeter": ("SP02", "bpm"),
            }


class status_code:
    def __init__(self) -> None:
        self.success = True 
        self.error = []


class deviceInfo:
    # def __init__(self, type, name, scale) -> None:
    def __init__(self, *args) -> None:  # type, name, scale (optional)
        self.type = args[0]
        self.name = args[1]
        self.serialNumber = None
        self.measurement = None

        # >> Should device check be here?

        # Check for unit scale (for now is just thermometer C/F)
        if len(args) == 3 and isinstance(args[2], str):
            # if args[2] == "C" or args[2] == "F":
            self.unit = args[2]
        else:
            self.unit = None

    # type = ""
    # name = ""
    # serialNumber = None
    # measurement = None

    def set_measurements(self, measurement):
        self.measurement = measurement
        self.measurementsTime = now.strftime("%d/%m/%Y %H:%M:%S")
    

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
    # check key (hardcoded for now)
    print(">> key ", key, keys)

    if key not in keys:
        status.success = False
        status.error.append("Invalid key")

    # check device type
    # print(device.type)
    valid_device = devices.get(device.type)    # returns device's units 

    # print(valid_device)
    # if device.type not in devices:
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

# Device interface skeleton - Celsius and Farenheit
from datetime import datetime
now = datetime.now()

keys = [
        "A1B2C3",
        "a1b2c3",
        "Z9Y8X7",
        "z9x8y7"
        ]

devices = (
            "thermometer", 
            "bp_monitor", 
            "w_scale", 
            "glucose_meter", 
            "oximeter"
            )


class status_code:
    success = True 
    error = []


class deviceInfo:

    # def __init__(self, type, name, scale) -> None:
    def __init__(self, *args) -> None:
        self.type = args[0]
        self.name = args[1]

        # Should device check be here?

        if isinstance(args[2],str):
            if args[2] == "C" or args[2] == "F":
                self.scale = args[2]
        else:
            self.scale = None

    # type = ""
    # name = ""
    serialNumber = ""

    def set_measurements(self,measurement):
        self.measurement = measurement
        self.measurementsTime = now.strftime("%d/%m/%Y %H:%M:%S")
    

def check_range(device):

    if device.type == "thermometer":
        if device.scale == "C" and device.measurement >= 45:
            return False
        elif device.scale == "F" and device.measurement >= 108.14:
            return False
    
    return True


def read_data(key, device, status):
    # check key (hardcoded for now)
    if key not in keys:
        status.success = False
        status.error.append("Invalid key")

    # check device type
    if device.type not in devices:
        status.success = False
        status.error.append("Invalid device type")

    # check measurements range
    if not check_range(device):
        status.success = False
        status.error.append("Invalid measurements")


# t = deviceInfo("thermometer", "t1", "C")
# print(t.type, t.name, t.scale)
# t.set_measurement(111)
# print(t.measurement)
# print(t.measurementsTime)
# status = status_code()
# read_data("a1b2c3", t, status)
# print(status.success, status.error)

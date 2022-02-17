# Device module tests
import os, sys

# getting the name of the directory where this file is present.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from devices import deviceInfo, read_data, status_code

# deviceInfo = {
#                 "name": str, *
#                 "type": str, *     Enum: [thermometer, bp_monitor, w_scale, glucose_meter, oximeter]
#                 "serial_number: int,
#                 "measurement": [int], 
#                 "unit": str, *
#                 "time_stamp": str
#               }


# Test 1 - device keys
def test_keys_auth():
    s1 = status_code()
    t1 = deviceInfo("thermo1", "thermometer", None, 36, "C")
    # t1.set_measurements(36)
    read_data("12345", t1, s1)
    expected = ['Invalid key']

    assert expected == s1.error


# Test 2 - Wrong type of device
def test_device_type():
    s2 = status_code()
    t2 = deviceInfo("BMI_1", "bmi_monitor", None, 100, "C")
    # t2.set_measurements(100)
    read_data("a1b2c3", t2, s2)
    expected = ['Invalid device type']

    assert expected == s2.error


# Test 3 - Wrong measurements range for thermometer
def test_thermo_C():
    s3 = status_code()
    t3 = deviceInfo("thermoC", "thermometer", None, 50.3, "C")
    # t3.set_measurements(50.3)
    read_data("a1b2c3", t3, s3)
    expected = ['Invalid measurements']

    assert expected == s3.error


def test_thermo_F():
    s4 = status_code()
    t4 = deviceInfo("thermoC", "thermometer", None, 200, "F")
    # t4.set_measurements(200)
    read_data("a1b2c3", t4, s4)
    expected = ['Invalid measurements']
    
    assert expected == s4.error


# Test 4 
def test_multiple_errors():
    s5 = status_code()
    t5 = deviceInfo("BMI_1", "bmi_monitor", None, None, None)
    read_data("a1b2c3123456", t5, s5)
    expected = ['Invalid key', 'Invalid device type', 'Invalid measurements']

    assert expected == s5.error


# Test - wrong scales for device type
def test_thermo_units():
    s6 = status_code()
    t6 = deviceInfo("t6", "thermometer", None, 30, "lbs")
    # t6.set_measurements(200)
    read_data("a1b2c3", t6, s6)
    expected = ['Invalid units for device']
    
    assert expected == s6.error

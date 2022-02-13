# Device module tests
import os, sys

# getting the name of the directory where this file is present.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from devices import deviceInfo, read_data, status_code

# keys = [
#         "12345",
#         "80801",
#         "A1B2C3"
#         "a1b2c3"
#         ]

status = status_code()


# Test 1 - device keys
def test_keys_auth():
    t1 = deviceInfo("thermometer", "thermo1", "C")
    read_data("12345", t1, status)
    expected = ['Invalid key']
    # captured = capsys.readouterr()

    assert expected == status.error


# Test 2 - Wrong type of device
def test_device_type():
    t2 = deviceInfo("bmi_monitor", "BMI_1")
    read_data("a1b2c3", t2, status)
    expected = ['Invalid device type']
    # captured = capsys.readouterr()

    assert expected == status.error


# Test 4 - Wrong measurements for device type
def test_thermo_C():
    t3 = deviceInfo("thermometer", "thermoC", "C")
    t3.set_measurements(50.3)
    read_data("a1b2c3", t3, status)
    expected = ['Invalid measurements']
    # captured = capsys.readouterr()

    assert expected == status.error


def test_thermo_F():
    t4 = deviceInfo("thermometer", "thermoF", "F")
    t4.set_measurements(200)
    read_data("a1b2c3", t4, status)
    expected = ['Invalid measurements']
    # captured = capsys.readouterr()
    
    assert expected == status.error


def test_multiple_errors():
    t5 = deviceInfo("bmi_monitor", "BMI_1")
    read_data("a1b2c3", t5, status)
    expected = ['Invalid device type']
    # captured = capsys.readouterr()

    assert expected == status.error


# Test - wront scales
def test_thermo_scales():
    t6 = deviceInfo("thermometer", "t5", "lbs")
    t6.set_measurements(200)
    read_data("a1b2c3", t6, status)
    expected = ['Invalid measurements']
    # captured = capsys.readouterr()
    
    assert expected == status.error

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


# Test 1 - device keys
def test_keys_auth():
    s1 = status_code()
    t1 = deviceInfo("thermometer", "thermo1", "C")
    t1.set_measurements(36)
    read_data("12345", t1, s1)
    expected = ['Invalid key']
    # captured = capsys.readouterr()

    assert expected == s1.error


# Test 2 - Wrong type of device
def test_device_type():
    s2 = status_code()
    t2 = deviceInfo("bmi_monitor", "BMI_1")
    t2.set_measurements(100)
    read_data("a1b2c3", t2, s2)
    expected = ['Invalid device type']
    # captured = capsys.readouterr()

    assert expected == s2.error


# Test 3 - Wrong measurements range for thermometer
def test_thermo_C():
    s3 = status_code()
    t3 = deviceInfo("thermometer", "thermoC", "C")
    t3.set_measurements(50.3)
    read_data("a1b2c3", t3, s3)
    expected = ['Invalid measurements']
    # captured = capsys.readouterr()

    assert expected == s3.error


def test_thermo_F():
    s4 = status_code()
    t4 = deviceInfo("thermometer", "thermoF", "F")
    t4.set_measurements(200)
    read_data("a1b2c3", t4, s4)
    expected = ['Invalid measurements']
    # captured = capsys.readouterr()
    
    assert expected == s4.error


# Test 4 
def test_multiple_errors():
    s5 = status_code()
    t5 = deviceInfo("bmi_monitor", "BMI_1")
    read_data("a1b2c3123456", t5, s5)
    expected = ['Invalid key', 'Invalid device type', 'Invalid measurements']
    # captured = capsys.readouterr()

    assert expected == s5.error


# Test - wrong scales for device type
def test_thermo_scales():
    s6 = status_code()
    t6 = deviceInfo("thermometer", "thermoScale", "lbs")
    t6.set_measurements(200)
    read_data("a1b2c3", t6, s6.error)
    expected = ['Invalid measurements']
    # captured = capsys.readouterr()
    
    assert expected == s6.error

# health-application

Jessica Martinez Marquez

## Description
Health platform to monitor patients' medical measurements and vital signs at home or in hospitals using third-party devices.
The goal is to provide interfaces to third-party medical devices to feed measurement readings into the system.

### Users & User Stories
- Patients
    - input device readings into system
    - schedule appointments with their health provider
    - communicate with health provider via text, video or voice message
    - access their medical measurements
- Medical professionals (nurses and doctors)
    - assign devices to patients
    - receive alerts from missed or abnormal device readings
    - access the transcription of patient's video or voice messages
    - search for keywords within transcription
    - access their appointements calendar
- Administrators
    - add users to the system and change their roles (patient, MP, admin, family member)
    - modify devices in the system (add, enable, disable, remove)
- Developers
    - access anonymized data 

### Modules
#### Device 
    - To create a device `deviceInfo("device_type", "device_name", "units", "serial_number")`

    | Parameter | Type | Options |
    |------|------| ------- |
    | device_type | String | see code block |
    | device_name | String | |
    | units (optional) | String | see code block |
    | serial number (optional) | Integer | |

    ``` 
    {
        "thermometer": ("C", "F"), 
        "bp_monitor": ("mmHg", "bpm"), 
        "w_scale": ("kgs", "lbs"), 
        "glucose_meter": "mg/dL", 
        "oximeter": ("SP02", "bpm"),
    }
    ```
    - To add device measurements `set_measurements(measurement)`

    | Parameter | Type |
    |------|------| 
    | measurement | Integer |

    - To read data `read_data(key, device, status)`

    | Parameter | Type |
    |------|------| 
    | key | String |
    | device | deviceInfo (created previously) |
    | status | status_code (created previously)| 

    - Status code `status_code()`

    | Member | Type |
    | ------ | ------ | 
    | success | Bool |
    | error | List of strings |
    
    Error messages:
    - Invalid key
    - Invalid device type
    - Invalid units for device
    - Invalid measurements

#### Calendar
#### Alerts
#### Communications
    - Chat 
    - Voice Transcriber
#### Administrative
#### Data Management
#### User Interface

## Branching Strategy
Each module is considered a feature. So, the branching strategy is the following:
- One branch per feature
- Will open a pull request to merge feature onto main to track its development
- Merge onto main when all unit tests have passed; therefore, at all times the main branch will work

## Tools
- pytest
- coverage
- linting with flake8
- logging
- cprofile

## References

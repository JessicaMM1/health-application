# Health Application

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

## Modules
### Device `/devices`

`https://health-app-2022.ue.r.appspot.com/`

- To read device data `(key, filename)`

    | Parameter | Description       |
    | --------- | ----------------- |
    | key       | String            |
    | filename  | JSON file (.json) |
  

- To create a device `(device_type, device_name, units, serial_number)`

    | Parameter     | Type    | Description                                |
    | ------------- | ------- | ------------------------------------------ |
    | device_type   | String  | Required. Check list of supported devices. |
    | device_name   | String  | Required                                   |
    | units         | String  | Required. Check list of supported units.   |
    | data          | Integer | Required                                   |
    | serial number | Integer | Optional                                   |

    Supported device types and units:
    - thermometer: ("C", "F") 
    - w_scale: ("kgs", "lbs") 
    - bp_monitor: ("mmHg", "bpm")
    - glucose_meter: "mg/dL"
    - oximeter: ("SP02", "bpm")
 
Error messages:
  - Invalid key
  - Invalid device type
  - Invalid units for device
  - Invalid measurements

Examples:
- Read data `/devices/<key>/<filename>`
  ```python
  {
    "name": "thermo1", 
    "type": "thermometer", 
    "serial_number": 12345, 
    "data": 33, 
    "unit": "C", 
    "time_stamp": "date_and_time"
  }  
  ```

### Chat

- Send messages between system users. 

    | Parameter | Type | Description |
    |------|------|------| 
    | recipient | String | Required. Account of recipient |
    | message type | String | Required. Supported types: text, image, audio, video |
    | content | String | Required. Body of message or url for media types |

    JSON Output:

    ```python 
    Text message
    {
        messageID: int
        sender: str
        recipient: str
        date: str
        time: str
        message_type: str
        body: str
        previous_msg: int
    }
    
    Media message
    {
        messageID: int
        sender: str
        recipient: str
        date: str
        time: str
        message_type: str
        url: str
        previous_msg: int
    }
    ```

    How to use:

    Text messages

    ```python
    {
        "recipient": "user123",
        "type": "text",
        "body": "Hello world!"
    }
    ```

    Media messages

    ```python
    {
        "recipient": "user123",
        "type": "image",
        "url": "url-of-your-image",
    }
    ```

    Error messages:
    - No recipient
    - Invalid message type
    - Invalid url

#### Calendar
#### Alerts
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

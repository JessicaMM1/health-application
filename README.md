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
- Device 
- Calendar
- Alerts
- Communications
    - Chat 
    - Voice Transcriber
- Administrative
- Data Management
- User Interface

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
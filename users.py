# User Module
from jsonschema import Draft6Validator
import json
import uuid


class User:

    def __init__(self, first_name, last_name, role) -> None:
        self.userID = str(uuid.uuid4())[0:8]
        self.first_name = first_name
        self.last_name = last_name
        # self.gender = gender
        self.role = role


class Doctor(User):

    def __init__(self, first_name, last_name, role) -> None:
        print("Creating doctor")
        super().__init__(first_name, last_name, role)
        self.patients = []

    def add_patient(self,patient):
        print("Adding patient ",patient.userID, " to list")
        self.patients.append(patient)

        for i in self.patients:
            print(i.__dict__)

    def remove_patient(self,uuid):
        print("Removing patient from list")
        self.patients.remove(uuid)


class Patient(User):
    def __init__(self, first_name, last_name, role) -> None:
        print("Creating patient")
        super().__init__(first_name, last_name, role)

        self.dob = None
        #self.age = None  # Would be better to calculate it
        self.medical_info = None
        self.my_doctor = None
        self.my_devices = None
       

class UserFactory:

    def json_validation():
        # add json validator here
        # validate(instance=json_input, schema=schema)
        # return dictionary
        pass

   
    def create_user(user_role):

        # res_dict = json_validation(json_input)
        # create user based on role & fill in attributes from dict
        # user_role = res_dict['role']

        if user_role == "doctor":
            return Doctor("Juana", "Banana", user_role)
        elif user_role == "patient":
            return Patient("Benito", "Bodoque", user_role)


# user_doc = UserFactory.create_user("doctor")
# print(user_doc.__dict__)

# user_patient1 = UserFactory.create_user("patient")
# print(user_patient1.__dict__)
# user_patient2 = UserFactory.create_user("patient")
# print(user_patient2.__dict__)
# user_doc.add_patient(user_patient1)
# user_doc.add_patient(user_patient2)

# test = {
#         "userInfo": {
#             "userID": 123,
#             "first_name": "Juana",
#             "last_name": "Banana"
#         },
#         "role": "doctorssss"

# }

# with open("users_schema.json", "r") as f:
#     schema = json.load(f)
#     # print(schema)
#     # Draft6Validator.check_schema(schema)
#     # Draft6Validator.check_schema(json.load(open("users_schema.json")))

# validator = Draft6Validator(schema)
# print(list(validator.iter_errors(test)))

# Draft6Validator(schema).validate(test)
#     Draft6Validator.check_schema(f)



# # User
# {
#     "userID": 123,
#     "first_name": "Sample",
#     "last_name": "User",
#     "gender": "Female",
#     "role": "Doctor"
# }

# Doctor
# {
#     "userInfo": {
#       "userID": 123,
#       "first_name": "Sample",
#       "last_name": "User",
#       "gender": "Female",
#       "role": "Doctor"
#     },
#      "patients": ["patient1", "patient2"]
# }

# # Patient
# {
#     "userInfo": {
#         "userID": 123,
#         "first_name": "Sample",
#         "last_name": "User",
#         "gender": "Female",
#         "role": "Patient"
#     },
#     "DOB": "01/01/2000",
#     "doctor": "doctor",
#     "devices": ["thermometer", "oximeter"],
#     "medical_info": [
#         { 
#             "medications": "Vitamin D",
#             "illnesses": "none"
#         }
#     ] 
# }

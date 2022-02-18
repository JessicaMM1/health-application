# Device API

from flask import Flask
from flask_restful import Resource, Api
from devices import status_code, read_data

status = status_code()

app = Flask("DeviceAPI")
api = Api(app)


class DeviceAPI(Resource):
    def get(self):
        return read_data("a1b2c3", "device1.json", status)


api.add_resource(DeviceAPI,"/")

if __name__ == '__main__':
    app.run(debug=True)

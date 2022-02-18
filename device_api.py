# Device API

from flask import Flask
from flask_restful import Resource, Api
from devices import status_code, read_data

status = status_code()

app = Flask("DeviceAPI")
api = Api(app)

# >> how to get unique status everytime get is called?


class DeviceAPI(Resource):
    def get(self, file):
        out = read_data("a1b2c3", file, status)
        if out is None:
            return status.error
        else:
            return out


api.add_resource(DeviceAPI,"/<string:file>")

if __name__ == '__main__':
    app.run(debug=True)

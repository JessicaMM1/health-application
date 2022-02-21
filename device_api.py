# Device API - web app

from flask import Flask
from flask_restful import Resource, Api, reqparse
from devices import add_data, status_code, read_data

app = Flask("DeviceAPI")
api = Api(app)

# Required arguments
device_put_args = reqparse.RequestParser()
device_put_args.add_argument("name", type=str, help="Name is required", required=True)
device_put_args.add_argument("type", type=str, help="Type is required", required=True)
device_put_args.add_argument("serial_number", type=int, help="Data is required", required=True)
device_put_args.add_argument("data", type=int, help="Data is required", required=True)
device_put_args.add_argument("unit", type=str, help="Data is required", required=True)


class DeviceAPI(Resource):
    def get(self, key, file):
        status_get = status_code()
        out = read_data(key, file, status_get)

        if out is None:   # if file does not exist
            return status_get.error
        else:
            return out


    def put(self, key, file):
        status_put = status_code()
        args = device_put_args.parse_args()
        add_data(key, args, file, status_put)
        # print(status_put.error)
        if not status_put.error:  # empty error list
            return "Writing to " + file, 200    # success
        else:
            return status_put.error, 400     # bad request


api.add_resource(DeviceAPI,"/<string:key>/<string:file>")

if __name__ == '__main__':
    app.run(debug=True)

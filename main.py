from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


class view(Resource):
    def get(self, data):
        response = '<p>You searched for: ' + data + '</p>'
        return response


api.add_resource(view, '/<string:data>')


if __name__ == '__main__':
    app.run(debug=False)
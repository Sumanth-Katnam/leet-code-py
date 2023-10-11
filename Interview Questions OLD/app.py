from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

errors = []

@app.route('/')
def hello():
    return "hello world", 200

@app.route('/errors')
def get_errors():
    print(errors)
    return jsonify({"errors": errors}), 200

@app.route('/temp', methods=['POST'])
def validate_overTemp():
    try:
        input_data = json.loads(request.data)["data"]
        data = input_data.split(':')
        formatted_time = datetime.fromtimestamp(int(data[1]) / 1000).strftime('%Y/%m/%d %H:%M:%S')
        print(data)
        if data[2] != "'Temperature'" or int(data[0])>>32 or int(data[1])>>64 or len(data) != 4:
            raise Exception
        if float(data[3]) > 90:
            return jsonify({"overtemp": "True", "device_id": data[0], "formatted_time": formatted_time}), 200
        else:
            return jsonify({"overtemp": "False"}), 200
    except:
        errors.append(input_data)
        return jsonify({"error": "bad request"}), 400


@app.route('/errors', methods=['DELETE'])
def clear_errorBuffer():
    errors.clear()
    return "", 200


if __name__ == '__main__':
    app.run()

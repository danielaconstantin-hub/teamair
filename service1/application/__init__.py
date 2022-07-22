from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/numbers', methods=['GET'])
def get_numbers():
    firsthalf = []
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    randomnum1 = random.randint(0,8)
    randomnum2 = random.randint(0,8)
    randomnum3 = random.randint(0,8)
    firsthalf.append(number[randomnum1])
    firsthalf.append(number[randomnum2])
    firsthalf.append(number[randomnum3])
    return Response(firsthalf, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
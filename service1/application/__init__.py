from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/numbers', methods=['GET'])
def get_numbers():
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randomnum = random.randint(0,9)
    return Response(number[randomnum], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
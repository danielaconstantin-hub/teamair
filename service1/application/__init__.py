from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/letters', methods=['GET'])
def get_letters():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    randomnum = random.randint(0,9)
    return Response(letter[randomnum], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')
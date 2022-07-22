from flask import Flask, Response
import random

app = Flask(__name__)

@app.route('/get/letters', methods=['GET'])
def get_letters():
    lasthalf = []
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    randomlet1 = random.randint(0,8)
    randomlet2 = random.randint(0,8)
    randomlet3 = random.randint(0,8)
    lasthalf.append(letter[randomlet1])
    lasthalf.append(letter[randomlet2])
    lasthalf.append(letter[randomlet3])
    return Response(lasthalf, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_num_let():
    number = (requests.get('http://localhost:5001/get/numbers')).text
    letter = (requests.get('http://localhost:5002/get/letters')).text
    
    return render_template('home.html', number=number, letter=letter)

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')
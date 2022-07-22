from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_num_let():
    number = (requests.get('http://service1:5001/get/numbers')).text
    letter = (requests.get('http://service2:5002/get/letters')).text

    num_let = f'{number} {letter}'

    message = (requests.post('http://service4:5004/result', data=num_let)).text
    
    return render_template('home.html', number=number, letter=letter, message=message)

if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')
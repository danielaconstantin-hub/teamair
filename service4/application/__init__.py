from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def get_result():
    
    num_let = request.data.decode('utf-8')

    answer = num_let.split(" ")

    letter = answer[1]

    number = answer[0]

    if number == '5' and letter == 'a':
        message = '5 and a'
    else:
        message = 'other'
    
    return Response(message, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5004, debug=True, host='0.0.0.0')
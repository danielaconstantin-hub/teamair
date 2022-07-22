from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def get_result():
    
    num_let = request.data.decode('utf-8')

    answer = num_let.split(" ")

    letter = answer[1]

    number = answer[0]

    if number[0] == '5' and number[1] == '5' or number[2] == '5' and number[1] == '5' or number[2] == '5' and number[0] == '5':
        message = 'password is not secure enough please generate a new one'
    elif letter[0] == 'A' and letter[1] == 'A' or letter[2] == 'A' and letter[1] == 'A' or letter[2] == 'A' and letter[0] == 'A':
        message = 'password is not secure enough please generate a new one'
    else:
        message = 'please use the above secure password'
    
    return Response(message, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5004, debug=True, host='0.0.0.0')
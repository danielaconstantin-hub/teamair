from application import app
from flask import Flask, Response
import random

@app.route('/get/numbers', methods=['GET'])
def get_numbers():
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    randomnum = random.randint(0,9)
    return Response(number[randomnum], mimetype='text/plain')
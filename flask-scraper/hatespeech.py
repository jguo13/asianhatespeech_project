from __future__ import print_function
import basc_py4chan
import pandas as pd
import os
import time
import sys
import copy
import csv 

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
hate_percentage = [
    {
        'percentage': 0
    }
]

DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/.well-known/pki-validation/BE5E7B3BAE09762ADC693A15C64B839F.txt', methods=['GET'])
def return_files_tut():
    if request.method == 'GET': 
        try:
            return send_file('BE5E7B3BAE09762ADC693A15C64B839F.txt', attachment_filename='BE5E7B3BAE09762ADC693A15C64B839F.txt')
        except Exception as e:
            return str(e)


@app.route('/get_hate/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/get_hate/stats', methods=['GET'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        len_hate = check_hate()
        response_object["percentage"] = len_hate
        return jsonify(response_object)
#define important variables


def check_hate():
    print("here")
    board_name = 'pol'
    try:
        list_hate = ['ABCs', 'ABC', 'spinks', 'spink', 'slopey', 'winks', 'slopes', 'slopies', 'slants', 'slopeheads', 'slant eyes', 'sideways vaginas', 'sideways cooters', 'sideways pussies', 'coolies', 'chonkies', 'chunkies', 'Chinese wetbacks', 'ching chongs', 'chinigs', 'chink a billies', 'chiggers', 'celestials', 'bamboo coons', 'chinig', 'sideways cooter', 'slopehead', 'chink a billy', 'Chinese wetback', 'bamboo coon', 'ching chong', 'coolie', 'slopy', 'chonky', 'chunky', 'sideways pussy', 'sideways vagina', 'chigger', 'slope', 'slant', 'slant eye', 'wink', 'celestial', 'whoriental', 'whorientals', 'gooky eyes', 'gooklets', 'gooklet', 'gookettes', 'gookette', 'gook eyed', 'gookies', 'gookie', 'goloids', 'goloid', 'ginks', 'gink', 'dog eaters', 'dog eater', 'yellow invaders', 'rice niggers', 'yellow invader', 'rice nigger']
        board = basc_py4chan.Board(board_name)
        all_thread_ids = board.get_all_thread_ids()
        thread_count = 0
        hate_count = 0
        for id in all_thread_ids:

            first_thread_id = id
            thread = board.get_thread(first_thread_id)
            if thread == None:
                continue
            topic = thread.topic
            for thread in thread.all_posts:
                thread_count += 1
                if any(s.lower() in thread.comment.lower() for s in list_hate):
                    hate_count += 1

        percentage = "{:.2%}".format(hate_count / thread_count)
        return percentage
    except :
        return "error with the server, please refresh"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
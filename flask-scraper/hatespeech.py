from __future__ import print_function
import basc_py4chan
import pandas as pd
import time
import sys
import copy
import csv
import os 

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
def check_thread(thread, set_hate):
    for s in set_hate:
        print(thread.comment.lower())
        if s.lower in thread.comment.lower():
            return True
    return False


def check_hate():
    filename1 = 'crawled_data_true.csv'
    filename2 = 'crawled_data_false.csv'
    if os.path.isfile(filename1):

        map_threads_true = set(pd.read_csv(filename1)["post_id"].to_list())
        map_threads_false = set(pd.read_csv(filename2)["post_id"].to_list())

    else:
        map_threads_true = set()
        map_threads_false = set()
    start_time = time.time()
    board_name = 'pol'
    try:

        set_hate = {'ABC', 'coolies', 'chink a billies', 'bamboo coons', 'chinig', 'slopehead', 'chink a billy', 'Chinese wetback', 'bamboo coon', 'ching chong', 'coolie', 'chigger', 'slope', 'slant', 'slant eye', 'wink', 'whoriental', 'gooklet', 'gookette', 'gook eyed', 'gookie', 'goloid', 'gink','dog eater', 'yellow invader', 'rice nigger'}
        board = basc_py4chan.Board(board_name)
        all_thread_ids = board.get_all_thread_ids()
        thread_count = 0
        hate_count = 0
        for id in all_thread_ids:

            thread_count += 1
            if id in map_threads_true:
                hate_count += 1
                continue
            if id in map_threads_false:
                continue

            thread = board.get_thread(id)
            if thread == None or thread.closed == True:
                thread_count += -1
                continue


            for threadcontent in thread.all_posts:
                if any(s.lower() in threadcontent.comment.lower() for s in set_hate):
                    hate_count += 1
                    map_threads_true.add(id)
                    break
                else:
                    map_threads_false.add(id)

        df1 = pd.DataFrame.from_dict(map_threads_true)
        df1.columns = ["post_id"]
        df1.to_csv(filename1, index=False)

        df2 = pd.DataFrame.from_dict(map_threads_false)
        df2.columns = ["post_id"]
        df2.to_csv(filename2, index=False)


        percentage = "{:.2%}".format(hate_count / thread_count)
        print("--- %s seconds ---" % (time.time() - start_time))

        return percentage
    except :
        return "error with the server, please refresh"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
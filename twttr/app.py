#!/usr/bin/python3
from flask import Flask, jsonify, render_template, request
import json
import os

app = Flask(__name__)
""" 
@app.before_request
def before_request():
    if request.path != '/':
        if request.headers['content-type'].find('application/json'):
            return 'Unsupported Media Type', 415
"""
@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/tweet', methods=['POST'])
def newTweet():
    if request.method == 'POST':
        tweetDict = request.get_json(silent=True)
        print("incoming tweet >>>>>:",tweetDict)
        return render_template('tweetSection.html')

 
@app.route('/tweetPost', methods=['POST'])
def tweetPost():
    print("POST!!!!!!")
    twtDict = request.get_json(silent=True)
    print(twtDict)
    if twtDict:
        tempJson = {}
        if (os.path.exists('./file.json')):
            with open('./file.json', 'r', encoding='utf-8') as readF:
                tempJson  = json.load(readF)
                tempJson.update(twtDict)
            with open('./file.json', "w", encoding='utf-8') as writeFile:
                f = json.dumps(tempJson)
                writeFile.write(f)
        else:
            print("File doesn't exist!")
            """with open('./file.json', "w+") as f:
                json.dump({}, f)"""
            with open('./file.json', "w") as wFile:
                f = json.dumps(twtDict)
                wFile.write(f)
    else:
        pass

    with open('./file.json', 'r', encoding='utf-8') as readF:
        posts  = json.load(readF)

    print(posts)
    print("Sending response!!!!")
    return jsonify(posts), 201


@app.route('/getTweets', methods=['GET'])
def getTweets():
    tempJson = {}
    if (os.path.exists('./file.json')):
        with open('./file.json', 'r', encoding='utf-8') as readF:
            tempJson  = json.load(readF)
    else:
        print("File doesn't exist!")

    print(tempJson)
    print("Sending response!!!!")
    return jsonify(tempJson), 201



 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

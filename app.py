#!/usr/bin/env python
import random
import time
import requests
import sys
import os
import logging 
import threading

from flask.helpers import send_file
from flask_restful import Resource, Api
from flask import Flask, request, jsonify, render_template



import json



app = Flask(__name__)


api=Api(app)
port=5000

if sys.argv.__len__()>1:
    port=sys.argv[1]
print ("You said port is :{}".format(port))

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    return "Successful Connection"



@app.route('/getscore',methods=['GET', 'POST'])
def getscore():
    data=request.get_json()
    url1=data['url1']
    url2=data['url2']
    userID=data['userID']
    postID=data['postID']
    model=data['model']
    
    r1 = requests.get(url1, allow_redirects=True)
    open('input1.mp4', 'wb').write(r1.content)

    r2 = requests.get(url2, allow_redirects=True)
    open('input2.mp4', 'wb').write(r2.content)

   
    os.system ('/openPose/run_mod.py --postID='+str(postID)+' --userID='+str(userID)+' --model='+str(model)+' --resize=432x368 --image=/openPose/images/')  
    os.system ('cp /openPose/output/output_full.mp4  /app/')  
  
   
    return 'Done'



if __name__ == "__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
    



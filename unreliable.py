#!/usr/bin/env python
import logging
#import yaml
import json
import datetime
import csv
import io
#from random import randint
import random
import time
from flask import Flask, request, Response
from threading import Thread

import sys

# HTTP_ERRORS = [200,404,408,500] 
HTTP_ERRORS = [404,408,500]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Crossref unreliable server'

@app.route('/foo')
def foo():
    e = random.choice(HTTP_ERRORS)
    return 'Crossref unreliable server:' + str(e),e

@app.route('/bar')
def bar():
    time.sleep(60*5)
    return 'Crossref unreliable server'

@app.route('/heartbeat')
def heartbeat():
    return json.dumps({"status":"OK"})

if __name__ == '__main__':

    # setup log
    logging.basicConfig(filename='log/unreliable.log',level=logging.DEBUG)

    # start our server
    logging.info("Unreliable starting")
    app.run(debug=True, use_reloader=False, port=5066)

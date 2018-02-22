from flask import Flask, render_template, url_for, redirect, request, flash
from flask import session as login_session
from flask import make_response, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import random
import string
import httplib2
import json
import requests

app = Flask(__name__)

# route to website homepage / category page
@app.route('/')
def showLanding():

    return render_template('landing_page.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template
import logging as log
from decouple import config
log.basicConfig(level=config('LOG_LEVEL'))



flaskAppInstance = Flask(__name__)

@flaskAppInstance.route("/")
def home():
    return render_template('home.html')   



if __name__ == '__main__':

    log.debug("Starting Flask Server")
    from api import *
    flaskAppInstance.run(host="0.0.0.0",port=5000,debug=False,use_reloader=True)
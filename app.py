from flask import Flask, render_template
import logging as log
# log.basicConfig(level='INFO')
# log.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
log.basicConfig(level=log.INFO,format='%(levelname)s-%(asctime)s-%(levelname)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')

flaskAppInstance = Flask(__name__)

@flaskAppInstance.route("/")
def home():
    return render_template('home.html')   



if __name__ == '__main__':

    log.debug("Starting Flask Server")
    from api import *
    flaskAppInstance.run(host="0.0.0.0",port=5000,debug=False,use_reloader=True)
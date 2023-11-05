from flask import Flask,request,render_template,jsonify
from Controller.user_Controller import home_api
import os
import pandas as pd
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(home_api)


if __name__ == "__main__":
    app.run()
    
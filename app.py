from flask import Flask, render_template, request
from model import predict_fields
import os
a = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/files'
a.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

@a.route("/")
def home():
    return render_template("index.html", pred="a")

@a.route("/result", methods = ['POST'])
def result():
    if request.method == "POST":
        value1 = request.form["value1"]
        value2 = request.form["value2"]
        value3 = request.form["value3"]
        value4 = request.form["value4"]
        value5 = request.form["value5"]
        value6 = request.form["value6"]
        value7 = request.form["value7"]
        value8 = request.form["value8"]
        value9 = request.form["value9"]
        value10 = request.form["value10"]
        value11 = request.form["value11"]
        value12 = request.form["value12"]
        value13 = request.form["value13"]
        value14 = request.form["value14"]
        value15 = request.form["value15"]
        all_values = [value1,
                value2, 
                value3,
                value4,
                value5,
                value6,
                value7,
                value8,
                value9,
                value10,
                value11,
                value12,
                value13,
                value14,
                value15]
        new = [int(x) for x in all_values]

        predection = predict_fields(new)
        return render_template("index.html", pred=predection)
    else:
        return render_template("index.html", pred = "a")


if __name__ == '__main__':
    a.run(debug=True)
from flask import Flask
from flask import request
import smtplib
import time


def gen_report():
    return "file.cls"
    pass


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/report', methods=['GET'])
def report():
    if request.method == 'GET':
        res = gen_report()
        return "<p>report generated</p><br><p>{res}</p>".format(res=res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

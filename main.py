from flask import Flask
from flask import request,jsonify,json
import requests
import smtplib
import time


def gen_report():
    return "file.cls"
    pass


app = Flask(__name__, static_url_path='/static')


@app.route("/<options>")
def getdata(options):
    if options=="codes":
        # url="https://gist.githubusercontent.com/mshafrir/2646763/raw/8b0dbb93521f5d6889502305335104218454c2bf/states_hash.json"
        # response = requests.get(url)
        f = open(f'{app.root_path}/static/states_hash.json', 'r')
        data = json.load(f)
        return data
    return "Error"

@app.route("/")
def hello_world():
    return "<p>Hello, World! hahahaah</p>"


@app.route('/report', methods=['GET'])
def report():
    if request.method == 'GET':
        res = gen_report()
        return "<p>report generated</p><br><p>{res}</p>".format(res=res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

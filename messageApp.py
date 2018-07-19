from flask import Flask, jsonify, request
app = Flask(__name__)


arry = []
@app.route('/message', methods=['GET','POST'])
def message():



    if request.method =='POST':
        arry.append(request.json["message"])
        resp = {
            "Allmessage": arry
        }
        return jsonify(resp)


    else:
        ress = {
            "Allmessage":arry
        }
        return jsonify(ress)




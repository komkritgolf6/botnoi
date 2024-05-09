from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "id": 1,
        "frameworks": "Django",
        "year": 2005
    },
    {
        "id": 2,
        "frameworks": "Flask",
        "year": 2010
    },
    {
        "id": 3,
        "frameworks": "Web2Py",
        "year": 2007
    }
]

@app.route('/postjsonbody', methods=['POST'])
def postjsonbody():
    if request.is_json:
        data = request.get_json()
        print(data)
        return 'success', 200
    else:
        return 'error', 400

@app.route('/postparams', methods=['POST'])
def postparams():
    params = request.args.to_dict()
    print(params)
    return 'success', 200

@app.route('/postformdata', methods=['POST'])
def postformdata():
    data = request.form.to_dict()
    print(data)
    return 'success', 200

@app.route('/postheader', methods=['POST'])
def postheader():
    headers = request.headers
    print(headers)
    return 'success', 200

@app.route('/getdata', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

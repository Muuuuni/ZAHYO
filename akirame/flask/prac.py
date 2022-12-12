from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route('/vrchat')
def data():
    req_data = request.args.to_dict()
    print(req_data)
    return jsonify(req_data)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def api_get():
    data = {"message": "pong"}
    return jsonify(data)

@app.route("/signin", methods=["POST"])
def api_siginin():


if __name__ == "__main__":
    app.debug = True
    app.run();

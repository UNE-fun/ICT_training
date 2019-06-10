from flask import Flask, jsonify

app = Flask(__name__)

#pingに飛ぶと、GET methodを使ってくれる
@app.route("/ping", methods=["GET"])
#この時に使う関数を定義
def api_get():
    #返してくれるデータを作成
    data = {"message": "pong"}
    #JSON形式で返す
    return jsonify(data)

#ぶっちゃけた話、これおまじない程度の認識です
if __name__ == "__main__":
    #デバッグを許可する
    app.debug = True
    #実行開始
    app.run();

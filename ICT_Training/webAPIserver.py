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

#signinに飛ぶと、POST methodを使ってくれる
#まだ書けてないこと：ユーザ認証情報を要求する
#                  ：認証情報にマッチしているアカウントがあるかDBから検索してくる
#                  ：アクセストークンを生成（個人個人別の値を与える）
#                  ：アクセス成功したらアクセストークンをJSON形式で返す
@app.route("/signin", methods=["POST"])
#この時に使う関数を定義
def api_signin():
    #とりあえずアクセストークンはhoge固定ってことで
    msg = "hoge"
    data = {"access_token": msg}
    return jsonify(data)

#ぶっちゃけた話、これおまじない程度の認識です
if __name__ == "__main__":
    #デバッグを許可する
    app.debug = True
    #実行開始
    app.run();

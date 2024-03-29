from flask import Flask, jsonify, request
from urllib.parse import urlparse
import mysql.connector
import hashlib

#立てているサーバがどこにあるのをここに書いておく
url = urlparse('mysql://user:password@127.0.0.1:3314/sample_db')

#dockerで立てたSQLサーバにアクセスする
conn = mysql.connector.connect(
    host = url.hostname or 'localhost',
    port = url.port or 3314,
    user = url.username or 'root',
    password = url.password or '',
    database = url.path[1:],
)

app = Flask(__name__)

#signinに飛ぶと実行すること
@app.route('/signin', methods=['POST'])
#この時に使う関数を定義
def api_signin():
    #postされてきたJSONデータを辞書型にパースする
    data = request.get_json()
    #print(data)
    #dataの中にあるuseridの中身の文字列を取得するなら・・・
    #data["userid"]
    cur = conn.cursor()
    msg = 'SELECT access_token FROM users WHERE userid="' + data["userid"] + '" AND password="' + hashlib.sha256(data["password"].encode()).hexdigest() + '"'
    #print(msg)
    cur.execute(str(msg))
    return jsonify(cur.fetchall())

#ぶっちゃけた話、これおまじない程度の認識です
if __name__ == "__main__":
    #デバッグを許可する
    app.debug = True
    #実行開始
    app.run();

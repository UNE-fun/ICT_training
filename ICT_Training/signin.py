from flask import Flask, jsonify
from urllib.parse import urlparse
import mysql.connector

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
@app.route("/signin", methods=["GET"])
#この時に使う関数を定義
def api_signin():
    #print(conn.is_connected())
    cur = conn.cursor()
    cur.execute('SELECT access_token FROM users')
    #print(cur.fetchall())
    return jsonify(cur.fetchall())

#ぶっちゃけた話、これおまじない程度の認識です
if __name__ == "__main__":
    #デバッグを許可する
    app.debug = True
    #実行開始
    app.run();

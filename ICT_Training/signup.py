from flask import Flask, jsonify, request
from urllib.parse import urlparse
import mysql.connector
import secrets

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
@app.route('/signup', methods=['POST'])
#この時に使う関数を定義
def api_signup():
    #postされてきたJSONデータを辞書型にパースする
    data = request.get_json()
    #print("受け取ったJSONデータ：")
    #print(data)

    #SQLを利用するのでcur宣言
    cur = conn.cursor()

    #access_tokenがかぶらないような文字れるであるまで生成する
    while(True):
        #access_tokenを生成する
        access_token = secrets.token_hex()
        #すでに存在しているアクセストークンでないことを確認
        msg = "SELECT access_token FROM users WHERE access_token='" + access_token + "'"
        cur.execute(str(msg))
        #かぶりがなかったら、[]が返される
        if(cur.fetchall()==[]):
            break

    

    #idの番号が今いくつが最大か取得してくる
    #print("idの最大値を取得してきます。")
    cur.execute('SELECT MAX(id) AS ID_MAX FROM users')
    id = cur.fetchall()
    #print("SQLから返されてきた結果：")
    #print(id[0][0]) #idが[(0,)]みたいになってたので無理やり調整

    #DBに追加したりするから、エラーが起きてしまった場合への処理も書いておく
    try:
        msg = "INSERT INTO users (id, userid, password, access_token) VALUES (" + str(id[0][0]+1) + ", '" + data["userid"] + "', '" + data["password"] + "', '" + access_token + "')"
        #print("DBに追加するときのSQL文：")
        #print(msg)
        cur.execute(str(msg))
        conn.commit()
    except:
        conn.rollback()
        raise

    #DBに確認しに行ってきて、取得できたaccess_tokenを表示する
    msg = "SELECT access_token FROM users WHERE userid='" + data["userid"] + "' AND password='" + data["password"] + "'"
    #print("DBに確認しに行くときのSQL文：")
    #print(msg)
    cur.execute(str(msg))
    return jsonify(cur.fetchall())

#ぶっちゃけた話、これおまじない程度の認識です
if __name__ == "__main__":
    #デバッグを許可する
    app.debug = True
    #実行開始
    app.run();

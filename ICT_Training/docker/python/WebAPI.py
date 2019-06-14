from flask import Flask
import uneget
import unesignin
import unesignup

app = Flask(__name__)

#pingに飛ぶと、GET methodを使ってくれる
@app.route("/ping", methods=["GET"])
def get():
    return uneget.api_get()

#signinに飛ぶとPOST methodを使う
@app.route("/signin", methods=["POST"])
#signin.pyを使う
def signin():
    return unesignin.api_signin()

#signupに飛ぶとPOST methodを使う
@app.route("/signup", methods=["POST"])
#signup.pyを使う
def signup():
    return unesignup.api_signup()

#ぶっちゃけた話、これおまじない程度の認識です
if __name__ == "__main__":
    #デバッグを許可して実行開始
    app.run("127.0.0.1", 5000, debug=True);

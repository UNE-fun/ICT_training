from flask import Flask, jsonify

#この時に使う関数を定義
def api_get():
    #返してくれるデータを作成
    data = {"message": "pong"}
    #JSON形式で返す
    return jsonify(data)

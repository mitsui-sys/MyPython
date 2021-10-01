#Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask,render_template, request

#Flaskオブジェクトの生成
app = Flask(__name__)


#「/」または「/index」へアクセスがあった場合に、「index.html」を返す
#ルーティングを統一
@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")  #クエリストリングからname属性の値を受け取る
    okyo = ["色不異空","空不異色","色即是空","空即是色"]  #okyoに般若心教を定義
    return render_template("index.html",name=name,okyo=okyo)  #okyoもhtml側に送る

# 「/index」にPOSTリクエストが来た場合
@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    okyo = ["色不異空", "空不異色", "色即是空", "空即是色"]
    return render_template("index.html", name=name, okyo=okyo)

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if __name__ == "__main__":
    app.run(debug=True)
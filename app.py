from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hello from Flask!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    print("受信したデータ:", data)

    #ここで統計処理

    return {"status": "ok", "received": data}

    

if __name__ == "__main__":
    app.run()
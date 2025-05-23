from flask import Flask, request, jsonify
import sqlite3
import uuid

app = Flask(__name__)

def insert_numbers(numbers):
    group_id = str(uuid.uuid4())
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        cur.executemany(
            "INSERT INTO numbers (number, group_id) VALUES (?, ?)",
            [(int(n), group_id) for n in numbers]
        )
    return group_id

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    numbers = data.get("numbers", [])
    if len(numbers) != 10 or not all(str(n).isdigit() and len(str(n)) == 3 for n in numbers):
        return jsonify({"status": "error", "message": "3桁の数字を10個入力してください"}), 400
    group_id = insert_numbers(numbers)
    return jsonify({"status": "success", "group_id": group_id})

if __name__ == '__main__':
    app.run(debug=True)

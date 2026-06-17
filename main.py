from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

problems_db = [
    {
        "id": 1,
        "title": "Low e-shop conversion rate",
        "parent_id": None
    },
    {
        "id": 2,
        "title": "Slow page load speed",
        "parent_id": 1
    },
    {
        "id": 3,
        "title": "Confusing checkout process",
        "parent_id": 1
    },
    {
        "id": 4,
        "title": "Unoptimized product images",
        "parent_id": 2
    }
]

@app.route("/")
def read_root():
    return jsonify({"message": "Flask backend for Problem Tree Analysis is running."})

@app.route("/api/nodes", methods=["GET"])
def get_nodes():
    return jsonify(problems_db)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

from flask import Flask, jsonify

app = Flask(__name__)

tasks_db = [
    {
        "id": 1,
        "title": "Spuštění e-shopu",
        "completed": False,
        "parent_id": None
    },
    {
        "id": 2,
        "title": "Návrh databáze",
        "completed": True,
        "parent_id": 1  # Tento uzel patří pod uzel s ID 1
    }
]

@app.route('/')
def read_root():
    return jsonify({'message': 'Ahoj z Flasku!'})

@app.route('/api/nodes', methods=['GET'])
def get_nodes():
    return jsonify(tasks_db)

if __name__ == '__main__':
    app.run(debug=True, port=8000)


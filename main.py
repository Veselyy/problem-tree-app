from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def read_root():
    return jsonify({'message': 'Ahoj z Flasku!'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)

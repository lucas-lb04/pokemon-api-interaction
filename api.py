from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "pokemon1":[
        {"id": 1, "reference": "Pikachu", "color": "yellow"},
        {"id": 2, "reference": "Charizard", "color": "red"},
        {"id": 3, "reference": "Tortank", "color": "blue"},
    ],

    "pokemon2":[
        {"id": 4, "reference": "Lucario", "color": "grey"},
        {"id": 5, "reference": "Gengar", "color": "Purple"},
        {"id": 6, "reference": "Darkrai", "color": "black"},
    ]
}

@app.route('/api/pokemon', methods=['GET'])
def get_pokemon():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
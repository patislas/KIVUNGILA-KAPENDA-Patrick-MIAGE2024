from flask import Flask, jsonify, request

app = Flask(__name__)


data = [
    {"ville": "lubumbashi", "pays": "rdc"},
    {"ville": "lusaka", "pays": "zambie"},
    {"ville": "kinshasa", "pays": "rdc"},
    {"ville": "new york", "pays": "usa"}
]

@app.route('/ville', methods=['PUT'])
def update_ville():
    return jsonify(data)

@app.route('/ville', methods=['DELETE'])
def delete_ville():
    return jsonify(data)


@app.route('/ville', methods=['GET'])
def get_ville():
    return jsonify(data)

@app.route('/ville', methods=['POST'])
def add_ville():
    new_ville = request.json
    if 'ville' in new_ville and 'pays' in new_ville:
        data.append(new_ville)
        return jsonify({"message": "ville ajouter avec succes", "ville": new_ville}), 201
    else:
        return jsonify({"erreur": "la ville et le pays n'ont pas ete enregistrer"}), 400

if __name__ == '__main__':
    app.run(debug=True)

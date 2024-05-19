from flask import Flask, jsonify, request

app = Flask(__name__)

cars = {
    1: {
        "name": "BMW",
        "price": 15000,
    },
    2: {
        "name": "Mercedes",
        "price": 3000,
    },
    3: {
        "name": "Audi",
        "price": 2900,
    }
}

@app.route('/cars', methods=['GET'])
def getCars():
    return jsonify(cars)

@app.route("/cars/<int:id>", methods=['GET'])
def getCarsById(id):
    if id in cars:
        return jsonify(cars[id])
    else:
        return jsonify("Car not found")

@app.route("/cars/<int:id>", methods=['PUT'])
def updateCarById(id):
    data = request.get_json()
    if id in cars:
        cars[id].update(data)
        return jsonify(cars[id])
    else:
        return jsonify("Car not found")

@app.route("/cars", methods=['POST'])
def addCar():
    data = request.get_json()
    cars.__setitem__(len(cars) + 1, data)
    return cars[len(cars)]

@app.route("/cars/<int:id>", methods=['DELETE'])
def deleteCar(id):
    if id in cars:
        del cars[id]
    return jsonify(cars)

app.run(port=5000, host='localhost', debug=False)
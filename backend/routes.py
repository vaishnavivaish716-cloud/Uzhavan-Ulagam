from flask import Blueprint, jsonify
prediction = Blueprint('prediction', __name__)
@prediction.route("/api/predict", methods=["POST"])
def predict():
    return jsonify({"result": "High chance of profit"})
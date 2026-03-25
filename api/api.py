from flask import Flask, request, jsonify, render_template
from prediction import predict_email

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    result = predict_email(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        # 👇 HERE is where request.form["news"] goes
        news = request.form["news"]

        data = vectorizer.transform([news])
        result = model.predict(data)
        prediction = "REAL NEWS 🟢" if result[0] == 1 else "FAKE NEWS 🔴"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
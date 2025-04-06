from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "1eaa4b974ab48c725af29bfbf6abbe35"  # Replace with your actual API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json()
                weather = {
                    "city": city,
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"]
                }
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
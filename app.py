from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    from_currency = request.form.get("from_currency")
    to_currency = request.form.get("to_currency")
    amount = float(request.form.get("amount"))

    from_currency_placeholder = from_currency
    to_currency_placeholder = to_currency
    amount_placeholder = amount

    response = requests.get(f"https://v6.exchangerate-api.com/v6/7d7b7d6ff63abda67e3e5cc3/latest/{from_currency}")
    data = response.json()

    if response.status_code == 200:
        rate = data["conversion_rates"][to_currency]
        result = amount * rate
        res = f"{result:,}"
        return render_template("indexPlus.html", res=res, from_currency_placeholder= from_currency_placeholder, to_currency_placeholder=to_currency_placeholder, amount_placeholder=amount_placeholder)
    else:
        error = "Can't reach the currency"
        return render_template("index.html", error=error)
    
@app.route("/version")
def version():
    return render_template("version.html")
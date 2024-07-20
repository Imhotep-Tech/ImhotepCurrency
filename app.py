from flask import Flask, render_template, request, jsonify, make_response, send_from_directory
from flask_sitemap import Sitemap
import requests
import datetime

app = Flask(__name__)
ext = Sitemap(app=app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    from_currency = request.form.get("from_currency")
    to_currency = request.form.get("to_currency")
    amount = float(request.form.get("amount"))
    
    if from_currency is None or to_currency is None or amount is None:
        error = "You have to fill all of the inputs!"
        return render_template("index.html", error=error)
    
    from_currency_placeholder = from_currency
    to_currency_placeholder = to_currency
    amount_placeholder = amount

    response = requests.get(f"https://v6.exchangerate-api.com/v6/12644ad30490895a4ffd9844/latest/{from_currency}")
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

@app.route('/sitemap.xml')
def sitemap():
    pages = []

    # Static pages
    ten_days_ago = (datetime.datetime.now() - datetime.timedelta(days=10)).date().isoformat()
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append(
                ["https://imhotepcc.vercel.app" + str(rule.rule), ten_days_ago]
            )

    sitemap_xml = render_template('sitemap_template.xml', pages=pages)
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"

    return response

@app.route('/static/_9b6a6904-b6cd-416b-88b1-ba3d981c9fed.ico')
def custom_static():
    return send_from_directory('static', '_9b6a6904-b6cd-416b-88b1-ba3d981c9fed.ico')

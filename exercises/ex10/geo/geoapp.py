from flask import Flask, render_template, request

app = Flask(__name__)


PYMI_LAT, PYMI_LONG = 10.8162109, 106.6941154


@app.route("/")
def index():
    """
    Truy cập website nhập param lat long vào URL:
    e.g: http://127.0.0.1:5000/?lat=51.505&long=-0.09
    """
    latitude = float(request.args.get("lat", PYMI_LAT))
    longitude = float(request.args.get("long", PYMI_LONG))

    return render_template("index.html", lat=latitude, long=longitude)


if __name__ == "__main__":
    app.run(debug=True)

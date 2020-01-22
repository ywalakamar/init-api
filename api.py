import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to the API</h1>"


app.run()

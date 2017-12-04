import flask, os
app = flask.Flask(__name__)

@app.route("/") # decorator specificies what to do when home.page/<decorator URL> is opened
def hello(): # what runs whenever home page is opened. can put parameters for this function
    return flask.render_template("index.html")

@app.route("/test")
def test():
    return flask.render_template("test.html")

if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

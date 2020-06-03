from flask import Flask
app = Flask(__name__)

@app.route("/")
def output():
    return "The text file has been formatted"

if __name__ == "__main__":
app.run()

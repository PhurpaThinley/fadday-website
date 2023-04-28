from flask import Flask

app = Flask(__name__)


@app.route("/")
def fadday():
  return "<p>About Fadday <p/>"


print(__name__)

if __name__ == "__main__":
  print("i am inside the name now")
  app.run(host='0.0.0.0', debug=True)

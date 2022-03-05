from flask import Flask

app = Flask(__name__)

@app.route("/") #this is the home page
def home():
  return "<h1>yo!</h1>"

if __name__ == "__main__":
  app.run()

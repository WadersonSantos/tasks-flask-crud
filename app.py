from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!!!"

@app.route("/about")  
def about():
  return "about the page"

@app.route("/a")  
def just_fun():
  return "Just for fun"
  

if __name__ == "__main__":
  app.run(debug=True)
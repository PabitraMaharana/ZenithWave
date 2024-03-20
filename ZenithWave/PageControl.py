from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("indexpage/index.html")

@app.route("/login")
def signin():
    return render_template("userlogin/signin.html")

@app.route("/signup")
def signup():
    return render_template("userlogin/signup.html")

@app.route("/videopage")
def video():
    return render_template("videopage/index.html")

@app.route("/listpage")
def list():
    return render_template("audiopage/podcast.html")

@app.route("/audiopage")
def audio():
    return render_template("audiopage/audio.html")

@app.route("/dashboardpage")
def dash():
    return render_template("dashboard/dashboard2.html")
    
if __name__ == "__main__":
    app.run(debug=True)
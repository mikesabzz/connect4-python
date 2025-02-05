# run the app with this command python3 app.py 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    player1_score = 0
    player2_score = 0
    return render_template("index.html", player1_score = player1_score, player2_score = player2_score)

if __name__ == "__main__":
    app.run(debug=True)

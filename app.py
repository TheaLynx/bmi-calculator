from flask import Flask, render_template, request

app = Flask(__name__)

# Definiere den Pfad für die Homepage

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

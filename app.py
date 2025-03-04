from flask import Flask, render_template, request

app = Flask(__name__)

# Definiere den Pfad für die Homepage

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Du bist untergewichtig - iss  mehr", "too-thin"
    elif bmi < 25:
        return "Du hast ein normales Gewicht - mach weiter so", "normal"
    else:
        return "Du bist übergewichtig - iss weniger und bewege dich mehr", "too-fat"

@app.route('/', methods=["GET", "POST"])
def index():
    bmi = None
    cat = None
    classy = None
    if request.method == 'POST':
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        bmi = round(weight / (height/100)**2, 2)
        cat, classy = categorize_bmi(bmi)

    return render_template('index.html', bmi=bmi, category=cat, classy=classy)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
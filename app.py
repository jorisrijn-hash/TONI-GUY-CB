from flask import Flask, render_template, request, jsonify

app = Flask(__name__)



def reageer(bericht):
    if "hoe gaat het" in bericht or "gaat het goed" in bericht:
        return "Goed hoor, bedankt!"
    elif "wat kan jij" in bericht:
        return "Ik kan vragen beantwoorden!"
    elif "naam" in bericht:
        return "Mijn naam is ChatBot 3000!"
    elif "afspraak" in bericht or "reserveren" in bericht or "boeken" in bericht:
        return "Wanneer wilt u langskomen? Kies een beschikbaar moment: AFSPRAAK_KNOPPEN"
    elif "weer" in bericht:
        return "Ik weet het niet, ik heb geen ramen!"
    elif "doei" in bericht or "bye" in bericht:
        return "STOP"
    elif "open" in bericht:
        return "De kapsalon is maandag tot zaterdag van 9:00 tot 18:00 uur geopend!"
    elif "gesloten" in bericht:
        return "De kapsalon is door de weeks vanag 18:00 tot 9:00 uur gesloten! Ook op zondag zijn we gesloten."
    elif "reserveren" in bericht:
        return "Wanneer wilt u langskomen? Kies een beschikbaar moment: AFSPRAAK_KNOPPEN"
    else:
        return "Dat snap ik niet, probeer iets anders."

@app.route("/")
def home():
    return render_template("index.html", welkom="Welkom bij HairMatters, hoe kan ik u helpen?")

@app.route("/chat", methods=["POST"])
def chat():
    bericht = request.json["bericht"].lower()
    antwoord = reageer(bericht)
    return jsonify({"antwoord": antwoord})

if __name__ == "__main__":
   import os
port = int(os.environ.get("PORT", 5001))
app.run(debug=False, host="0.0.0.0", port=port)
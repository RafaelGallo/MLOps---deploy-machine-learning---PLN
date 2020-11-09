from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob

app = Flask(__name__)
app.config["BASIC_AUTH_USERNAME"] = 'alfa'
app.config["BASIC_AUTH_PASSWORD"] = 'mega'
basic_auth = BasicAuth(app)

@app.route("/")
def home():
    return "Deploy machine learning - Processo de linguagem natural"

@app.route("/sentimento/<frase>")
@basic_auth.required

def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to = "en")
    polaridade = tb_en.sentiment.polarity
    return "polaridade: {}".format(polaridade)

app.run(debug=True)
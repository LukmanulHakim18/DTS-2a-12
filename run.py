from os import name
from flask import Flask, render_template
import requests
import re

app = Flask(__name__)

urlApi = {
    "indonesia": "https://api.kawalcorona.com/indonesia",
    "globalPositif": "https://api.kawalcorona.com/positif",
    "globalSembuh": "https://api.kawalcorona.com/sembuh",
    "globalMeninggal": "https://api.kawalcorona.com/meninggal",
}


def dataIndonesia():
    data = requests.get(urlApi['indonesia']).json()
    return data[0]


def dataGlobalPositif():
    data = requests.get(urlApi['globalPositif']).json()
    number = re.sub('[^0-9]', '', data['value'])
    return int(number)


def dataGlobalSembuh():

    data = requests.get(urlApi['globalSembuh']).json()
    number = re.sub('[^0-9]', '', data['value'])
    return int(number)


def dataGlobalMeninggal():
    data = requests.get(urlApi['globalMeninggal']).json()
    number = re.sub('[^0-9]', '', data['value'])
    return int(number)


@app.route("/")
def index():
    return render_template("index.html",
                           dataIndonesia=dataIndonesia(),
                           dataGlobalPositif=dataGlobalPositif(),
                           dataGlobalSembuh=dataGlobalSembuh(),
                           dataGlobalMeninggal=dataGlobalMeninggal()
                           )


if __name__ == "__main__":
    app.run(debug=True)

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
    "provinsi": "https://api.kawalcorona.com/indonesia/provinsi",
}


def dataIndonesia():
    data = requests.get(urlApi['indonesia']).json()
    return data[0]


def dataGlobalPositif():
    data = requests.get(urlApi['globalPositif']).json()
    number = re.sub('[^0-9]', '', data['value'])
    return number


def dataGlobalSembuh():

    data = requests.get(urlApi['globalSembuh']).json()
    number = re.sub('[^0-9]', '', data['value'])
    return int(number)


def dataGlobalMeninggal():
    data = requests.get(urlApi['globalMeninggal']).json()
    number = re.sub('[^0-9]', '', data['value'])
    return int(number)


def dataProvinsiRiau(dataIndonesia):
    dataIndonesia = dataIndonesia
    data = requests.get(urlApi['provinsi']).json()
    newData = data[8]['attributes']
    newData['persentasiPositif'] = newData['Kasus_Posi'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['positif']))
    newData['persentasiSembuh'] = newData['Kasus_Semb'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['sembuh']))
    newData['persentasiMeninggal'] = newData['Kasus_Meni'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['meninggal']))
    newData['persentasiPositif'] = round(newData['persentasiPositif'], 4)
    newData['persentasiSembuh'] = round(newData['persentasiSembuh'], 4)
    newData['persentasiMeninggal'] = round(newData['persentasiMeninggal'], 4)

    return newData


def dataProvinsiNTB(dataIndonesia):
    dataIndonesia = dataIndonesia
    data = requests.get(urlApi['provinsi']).json()
    newData = data[24]['attributes']
    newData['persentasiPositif'] = newData['Kasus_Posi'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['positif']))
    newData['persentasiSembuh'] = newData['Kasus_Semb'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['sembuh']))
    newData['persentasiMeninggal'] = newData['Kasus_Meni'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['meninggal']))
    newData['persentasiPositif'] = round(newData['persentasiPositif'], 4)
    newData['persentasiSembuh'] = round(newData['persentasiSembuh'], 4)
    newData['persentasiMeninggal'] = round(newData['persentasiMeninggal'], 4)

    return newData


def dataProvinsiSulut(dataIndonesia):
    dataIndonesia = dataIndonesia
    data = requests.get(urlApi['provinsi']).json()
    newData = data[15]['attributes']
    newData['persentasiPositif'] = newData['Kasus_Posi'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['positif']))
    newData['persentasiSembuh'] = newData['Kasus_Semb'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['sembuh']))
    newData['persentasiMeninggal'] = newData['Kasus_Meni'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['meninggal']))
    newData['persentasiPositif'] = round(newData['persentasiPositif'], 4)
    newData['persentasiSembuh'] = round(newData['persentasiSembuh'], 4)
    newData['persentasiMeninggal'] = round(newData['persentasiMeninggal'], 4)

    return newData


def dataProvinsiJateng(dataIndonesia):
    dataIndonesia = dataIndonesia
    data = requests.get(urlApi['provinsi']).json()
    newData = data[2]['attributes']
    newData['persentasiPositif'] = newData['Kasus_Posi'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['positif']))
    newData['persentasiSembuh'] = newData['Kasus_Semb'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['sembuh']))
    newData['persentasiMeninggal'] = newData['Kasus_Meni'] / \
        int(re.sub('[^0-9]', '', dataIndonesia['meninggal']))
    newData['persentasiPositif'] = round(newData['persentasiPositif'], 4)
    newData['persentasiSembuh'] = round(newData['persentasiSembuh'], 4)
    newData['persentasiMeninggal'] = round(newData['persentasiMeninggal'], 4)

    return newData


@app.route("/")
def index():
    return render_template("index.html",
                           dataIndonesia=dataIndonesia(),
                           dataGlobalPositif=dataGlobalPositif(),
                           dataGlobalSembuh=dataGlobalSembuh(),
                           dataGlobalMeninggal=dataGlobalMeninggal(),
                           dataProvinsiRiau=dataProvinsiRiau(dataIndonesia()),
                           dataProvinsiSulut=dataProvinsiSulut(
                               dataIndonesia()),
                           dataProvinsiJateng=dataProvinsiJateng(
                               dataIndonesia()),
                           dataProvinsiNTB=dataProvinsiNTB(dataIndonesia())
                           )


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

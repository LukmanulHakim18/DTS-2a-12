import requests
import re


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
    return newData


print(dataProvinsiRiau(dataIndonesia()))

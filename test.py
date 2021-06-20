import requests
import re

urlApi = {
    "indonesia": "https://api.kawalcorona.com/indonesia",
    "globalPositif": "https://api.kawalcorona.com/positif",
    "globalSembuh": "https://api.kawalcorona.com/sembuh",
    "globalMeninggal": "https://api.kawalcorona.com/meninggal",
}


def dataIndonesia():
    data = requests.get(urlApi['indonesia']).json()
    return data[0]


def dataGlobalSembuh():
    data = requests.get(urlApi['globalSembuh']).json()
    number = re.sub('[^0-9]', '', data['value'])
    return int(number)


print(dataGlobalSembuh())

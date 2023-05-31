from flask import Flask
import json
from flask import request
import requests
app = Flask(__name__)

converter = {
        'real': "", 
        'dolar': '',
        'euro': ""
}
    


@app.route('/', methods=['GET'])
def get_dolar():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    response = requests.get(url)
    dataUsd = response.json()
    currency = dataUsd['USDBRL']['bid']
    converter["dolar"] = currency
    url = 'https://economia.awesomeapi.com.br/last/EUR-BRL'
    response = requests.get(url)
    dataEur = response.json()
    currency = dataEur['EURBRL']['bid']
    converter["euro"] = currency
    return json.dumps(converter)



@app.route('/convertemoeda/<valor>')
def show_currency(valor):
    converter["real"] = valor
    converter['dolar'] = converter['dolar'] * valor
    converter['euro'] = converter['euro'] * valor
    return json.dumps(converter)  
if __name__ == "__main__":
    app.run()
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_json():
    # Obtenha a data e o estado da URL
    date = request.args.get('date', '02/09/2023')
    state = request.args.get('state', 'RJ')

    url = "https://api.pontodobicho.com/results"
    
    # Dicionário para armazenar o resultado
    resultado = {}

    querystring = {"date": date, "state": state}
    payload = ""
    headers = {
        "authority": "api.pontodobicho.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "_fbp=fb.1.1690503295318.1646712376; _ga=GA1.1.1949527877.1690503308; _gcl_au=1.1.1735863997.1690503308; __e_inc=1; _ga_P8C4RJ0F48=GS1.1.1693747980.3.1.1693747983.0.0.0",
        "origin": "https://www.pontodobicho.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "x-client-version": "1.30"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    json_res = response.json()
    
    # Armazenar o resultado no dicionário
    resultado['date'] = date
    resultado['state'] = state
    resultado['data'] = json_res

    # Salvar o resultado como um arquivo JSON
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(resultado, json_file, ensure_ascii=False, indent=4)
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

import requests
import json
import sys
from datetime import date

wheater_site_url = 'http://api.openweathermap.org/data/2.5/forecast?'
params = {
    'q': '',
    # 'lat': '',
    # 'lon': '',
    'appid': '5480412bb20e1c99fd10d525a1633add',
    'cnt': '',
    'mode': 'json',
    'lang': 'pt_br',
    'units': 'metric' #for celsius 
}


def parse_json(json_file) -> str:
    return json.loads(json_file)


def request_weather(params: dict) -> None:
    '''
        request weather of the city pass by params dictionary
        this function will use request module to get page content
        and it will be convert the data using another function parse_json
    '''
    res = requests.get(wheater_site_url, params=params)
    res.raise_for_status()

    # data = obj json where contais a list of each day
    data = parse_json(res.text)
    data = data['list']
    main_info = data[0]['main']
    weather = data[0]['weather']

    #print(main_info)
    #print(weather)

    today = date.today()

    info = {
        'temp': '',
        'feels_like': '',
        'temp_min': '',
        'temp_max': '',
        'humidity': '', 
        'description': '',
    }



    for idx in data:

        for key, value in idx['main'].items():
            if key in info:
                info[key] = value
            
        weather_list = idx['weather']


    print(info)

        




def main():
    if len(sys.argv) < 2:
        print('Entrada invalida.\nModo de uso: python weather_request.py cidade (opcional)quantidade_de_dias(max:5)')
        sys.exit(1)
    
    params['q'] = sys.argv[1]
    params['cnt'] = sys.argv[2]
    request_weather(params)



if __name__ == '__main__':
    main()
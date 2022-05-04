import requests
import json
import sys
from datetime import date, datetime, timedelta

wheater_site_url = 'http://api.openweathermap.org/data/2.5/forecast?'
params = {
    'q': '',
    # 'lat': '',
    # 'lon': '',
    'appid': '5480412bb20e1c99fd10d525a1633add',
    'cnt': '1',
    'mode': 'json',
    'lang': 'pt_br',
    'units': 'metric' #for celsius 
}


def parse_json(json_file) -> str:
    ''' simple convert the json file into python data '''
    return json.loads(json_file)




def print_dict(data: list) -> None:
    ''' will print formated data from dict to user '''

    d = date.today()
    for x in data:
        print(f'''
            Date: {d.strftime('%d/%m/%Y')}
            Temperature: {x['temp']}
            Min: {x['temp_min']}, Max: {x['temp_max']}
            Feels like: {x['feels_like']}%
            Humidity: {x['humidity']}
            Description: {str(x['description']).capitalize()}\n''')
        d += timedelta(days=1)



def request_weather(params: dict) -> None:
    '''
        request weather of the city pass by params dictionary
        this function will use request module to get page content
        and it will be convert the data using another function parse_json
    '''
    try:
        res = requests.get(wheater_site_url, params=params)

        # data = obj json where contais a list of each day
        data = parse_json(res.text)
        data = data['list']

        info = {
            'temp': '',
            'feels_like': '',
            'temp_min': '',
            'temp_max': '',
            'humidity': '', 
            'description': '',
        }

        array_of_info = []

        # passing throght data extract from json
        for idx in data:
            new_info = {}

            # idx['main'] = dictionay 
            for key, value in idx['main'].items():
                # if the key in the dictonary is the same as the info, insert the value
                if key in info:
                    new_info[key] = value

            # weather info it is inside a dict named as 'wather', wich contains a single array
            # inside this array contais a dict, wich has the info that we are looking for        
            weather_dict = idx['weather'][0]
            for key, value in weather_dict.items():
                if key in info:
                    new_info[key] = value

            array_of_info.append(new_info)

        print_dict(array_of_info)

    except:
        print('City not found. Try a valid one.')
        sys.exit(1)
        

        




def main():
    if len(sys.argv) < 2:
        print('Entrada invalida.\nModo de uso: python weather_request.py city (optional)number_of_days(max:5)')
        sys.exit(1)
    
    params['q'] = sys.argv[1]
    if len(sys.argv) > 2: 
        params['cnt'] = sys.argv[2]
    request_weather(params)



if __name__ == '__main__':
    main()
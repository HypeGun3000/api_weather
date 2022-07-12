import requests


def main():
    payloud = {
        'nTqm': '',
        'lang': 'ru',
    }

    list_of_weather_places = ['https://wttr.in/london',
                              'https://wtt1r.in/svo',
                              'https://wttr.in/Череповец']

    for weather_place in list_of_weather_places:
        try:
            response = requests.get(weather_place, params=payloud)
            print(response.text)
        except:
            raise ConnectionError(f'Ошибка подключения!')


if __name__ == '__main__':
    main()

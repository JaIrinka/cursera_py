# *****************************
#         КЛАССЫ - 6
# возможно, доделаю. Пока висит этот коммент - код не рабочий)
# *****************************
import requests
import sys
import pprint

API_KEY_YANDEX_WEATHER = '4ef3d082-ec51-4a3a-a5fa-db58613a9ef4'
FIELDS = ["temp_max", "temp_min"]


class YandexWeatherForecast:
    """
    класс для работы с API ЯндексПогоды, страница документации API -
    https://yandex.ru/dev/weather/doc/dg/concepts/forecast-test.html/
    """

    URL = 'https://api.weather.yandex.ru/v2/informers?'

    def __init__(self, key):
        self.key = key
        self.headers = {'X-Yandex-API-Key': key}

    def get_weather_week_forecasts(self, city, fields):
        """возвращает список с недельным прогнозом погоды для населенного пункта city,
        необходимые характеристики погоды передаются в списке fields"""

        data = requests.get(f'{self.URL}lat=59.9386&len=30.3141', headers=self.headers)
        print(data)

        week_forecast = []

#        for forecast in data['forecasts']:
#            data = {'date': forecast["date"]}
#            for field in fields:
#                value = forecast["parts"]["day"].get(field, None)
#                if value is not None:
#                    data[field] = value
#            week_forecast.append(data)

        return week_forecast


class CityInfo:

    def __init__(self, city, forecast_provider):
        self.city = city
        self._forecast_provider = forecast_provider

    def weather_forecast(self, fields):
        return self._forecast_provider.get_weather_week_forecasts(self.city, fields)


def _main():
    weather_api = YandexWeatherForecast(API_KEY_YANDEX_WEATHER)
    city_info = CityInfo('omsk', weather_api)
    forecast = city_info.weather_forecast(FIELDS)
    pprint.pprint(forecast)


if __name__ == "__main__":
    _main()

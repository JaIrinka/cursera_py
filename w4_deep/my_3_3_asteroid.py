# *****************************
# ДЛЯ ЭТОГО КЛАССА БУДЕМ ПИСАТЬ СЛЕДУЮЩИЙ ТЕСТ
# *****************************
import requests


class Asteroid:
    BASE_API_KEY_URL = 'https://api.nasa.gov/neo/rest/v1/neo/{}?api_key=DEMO_KEY'

    def __init__(self, spk_id):
        self.api_url = self.BASE_API_KEY_URL.format(spk_id)

    def get_data(self):
        return requests.get(self.api_url).json()

    def write_data_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(requests.get(self.api_url).text)

    @property
    def name(self):
        return self.get_data()['name']

    @property
    def diameter(self):
        return int(self.get_data()['estimated_diameter']['meters']['estimated_diameter_max'])


if __name__ == '__main__':
    apophis = Asteroid(2099942)

    apophis.write_data_to_file('apophis_test_file.txt')
    print(f'Name: {apophis.name}')
    print(f'Diameter: {apophis.diameter}m')

# *****************************
#         ТЕСТИРОВАНИЕ
# юнит-тест для астероида
#
# https://docs.python.org/3/library/unittest.mock.html
# https://docs.python.org/3/library/unittest.mock-examples.html
# *****************************
import json
import unittest
from unittest.mock import patch

from my_3_3_asteroid import Asteroid


class TestAsteroid(unittest.TestCase):
    def setUp(self):
        """ готовим тестовые данные """
        self.asteroid = Asteroid(2099942)

    def mocked_get_data(self):
        """ тут делаем мок - вместо запроса в интернет будет произведён запрос в файл """
        with open('apophis_test_file.txt') as f:
            return json.loads(f.read())

    @patch('my_3_3_asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        """ декоратор добавляет в качестве мока для метода,
            указанного в первом аргументе метод,
            указанный во втором аргументе """
        self.assertEqual(
            self.asteroid.name,
            '99942 Apophis (2004 MN4)'
        )

    @patch('my_3_3_asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        self.assertEqual(self.asteroid.diameter, 682)

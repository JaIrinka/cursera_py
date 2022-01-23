# *****************************
#           ИСКЛЮЧЕНИЯ
#
# запуск реквестера:
# python3 my_3_exceptions.py http://github.com
#
# https://docs.python.org/3/tutorial/errors.html
# https://docs.python.org/3/library/exceptions.html
# *****************************
import traceback
import sys
import requests


def requester():
    url = sys.argv[1]

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.Timeout:
        print(f'ошибка timeout url={url}')
    except requests.HTTPError as err:
        code = err.response.status_code
        print(f'ошибка url: {url}, code: {code}')
    except requests.RequestException:
        print(f"ошибка скачивания url: {url}")
    else:
        print(response.content)


def exceptions_ex1():
    while True:
        try:
            raw = input("введите число: ")
            number = int(raw)
            print(f"вы ввели {number}")
            break
        except ValueError as err:
            trace = traceback.print_exc()
            print(trace)
            print(err)
            print("некорректное значение!")
        except KeyboardInterrupt:
            print("ВЫХОД")
            break


#exceptions_ex1()
# если запускаем реквестор, эксцепшен лучше закомментить и наоборот
requester()

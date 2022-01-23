# *****************************
#     ОТЛАДКА / DEBUG
# python -m pdb my_3_1_debug.py
# можно дебажить в пайчарме или другой IDE
#
# https://docs.python.org/3/library/pdb.html
# *****************************
import re
import requests


def main(site_url, substring):
    site_code = get_site_code(site_url)
    matching_substrings = get_matching_substring(site_code, substring)
    print(f'{substring} found {len(matching_substrings)} times in {site_url}')


def get_site_code(site_url):
    if not site_url.startswith('http'):
        site_url = 'http://' + site_url

    return requests.get(site_url).text


def get_matching_substring(source, substring):
    return re.findall(substring, source)


if __name__ == "__main__":
    main('mail.ru', 'script')

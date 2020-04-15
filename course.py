import requests
from bs4 import BeautifulSoup


class Dollar:
    DOLLAR_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk02twJQ4QxMOgb3MfN1h6Z1VYBTulQ%3A1585752981080&ei=lauEXsO7BIu-tQb0oJfABQ&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIKCAAQgwEQRhCCAjIFCAAQgwEyAggAMgIIADIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADoHCAAQgwEQQzoECAAQQ1CZDFjjLWD4MGgCcAB4A4AByguIAYopkgELMy00LjQuMS4wLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiD2o2ZvsfoAhULX80KHXTQBVgQ4dUDCAs&uact=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.dollor_value = 78.5
        self.current_dollor = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return convert[0].text.replace(',', '.')


class Hryvnia:
    HRYVNIA_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk00Fk4_WMw9g2y40QQF69twZtU8wEA%3A1585768681965&ei=6eiEXum3OpLA0PEPqcyR-AI&q=%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1D-A1jnHmCHIWgCcAB4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab&ved=0ahUKEwip0O_X-MfoAhUSIDQIHSlmBC8Q4dUDCAs&uact=5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.hryvnia_value = ' '
        self.current_hryvnia = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.HRYVNIA_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return convert[0].text.replace(',', '.')


class Euro:
    EURO_RUB = 'https://www.google.com/search?newwindow=1&rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk03TSWxu1WWL5kOOKuhjSshdf2fqtQ%3A1586976625104&ei=cVeXXu38BcnQ6QTj1bKgBg&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%83%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQARgAMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKOgQIABBHOgYIABAHEB5KEQgXEg0xMC0xODZnMTY4ZzE2SgwIGBIIMTAtMWcxZzJQwf0MWPmEDWDEkQ1oAHACeAGAAewFiAGACpIBBzAuMy42LTGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.euro_value = ' '
        self.current_euro = float(self.get_currency_price())

    def get_currency_price(self):
        full_page = requests.get(self.EURO_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return convert[0].text.replace(',', '.')
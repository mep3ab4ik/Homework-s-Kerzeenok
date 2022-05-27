import json
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, asdict


url = 'https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-online'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.64 ',
}


@dataclass
class Info:
    title: str
    text_info: list



def main():

    # Передаем наш url. В headers добавляем User-Agent для получение ответа 200
    r = requests.get(
        url=url,
        headers=headers
    )

    # очищаем от html кода и оставляем все чистое
    soup = BeautifulSoup(r.text, 'html.parser')

    # ищем данные в блок div, который имеет класс нужный нам класс
    all_soup = soup.find_all('div', class_='t517__sectioninfowrapper')
    topic = []

    # Бегаем по блоку
    for i in all_soup:
        # Ищем блок div c этим классом
        title = i.find('div', class_='t-name')
        # Ищем все атрибуты li
        text = i.find_all('li')
        text_info = []

        # Бегаем по атрибутам li. Забираем из них текст и очищаем от пробелов( в некоторых местах они есть)
        for t in text:
            text_info.append(t.text.strip())
        # Добавляем в строку с помощью asdict
        topic.append(asdict(Info(title.text, text_info)))
    # Возвращаем json. ensure_ascii в False, т.к ensure_ascii в True возвращает символы не ASCII
    return json.dumps(topic, indent=0, ensure_ascii=False)


if __name__ == '__main__':
    print(main())
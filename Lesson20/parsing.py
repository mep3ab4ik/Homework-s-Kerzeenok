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
    r = requests.get(
        url=url,
        headers=headers
    )

    soup = BeautifulSoup(r.text, 'html.parser')

    all_soup = soup.find_all('div', class_='t517__sectioninfowrapper')
    topic = []

    for i in all_soup:
        title = i.find('div', class_='t-name')
        text = i.find_all('li')
        text_info = []

        for t in text:
            text_info.append(t.text.strip())

        topic.append(asdict(Info(title.text.strip(), text_info)))
    return json.dumps(topic, indent=0, ensure_ascii=False)

if __name__ == '__main__':
    print(main())
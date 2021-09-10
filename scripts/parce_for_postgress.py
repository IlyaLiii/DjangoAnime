import psycopg2
from bs4 import BeautifulSoup
import requests as req
import time
import datetime
from contextlib import closing

url = 'https://shikimori.one/collections/3981-200-samyh-populyarnyh-anime-na-shikimori'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36',
    'accept': '*/*'
}


class Parce:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_html(self):
        request = req.get(self.url, headers=self.headers)
        return request

    def get_content(self, html):
        soup = BeautifulSoup(html, 'lxml')
        # Получаем ссылки на тайтлы,чтобы дальше парсить
        links = soup.find_all('article')
        list_of_hrefs = []
        for a in links:
            title = a.find('a').get('href')
            list_of_hrefs.append(title)
        list_of_hrefs.remove(None)

        return list_of_hrefs

    def get_data(self, list_with_links):
        data = {}
        i = 1
        for link in list_with_links:
            request = req.get(link, headers=headers)
            soup = BeautifulSoup(request.text, 'lxml')

            name_of_title = soup.find('h1').get_text().replace('/', '').split('  ')
            name_ru = name_of_title[0]
            # print(name_ru)
            name_eng = name_of_title[1]
            try:
                rating = soup.find('div', class_='score-value score-9').get_text()
            except(AttributeError):
                try:
                    rating = soup.find('div', class_='score-value score-8').get_text()
                except(AttributeError):
                    try:
                        rating = soup.find('div', class_='score-value score-7').get_text()
                    except(AttributeError):
                        rating = soup.find('div', class_='score-value score-6').get_text()
            genres = soup.find_all('span', class_='genre-ru')
            genres_list = []
            for genre in genres:
                genres_list.append(genre.get_text())
            # print(genres_list)
            try:
                status = soup.find('span', class_='b-anime_status_tag released').get('data-text').capitalize()
            except(AttributeError):
                status = soup.find('span', class_='b-anime_status_tag ongoing').get('data-text').capitalize()
            if soup.find('div', class_='line-container').get_text().replace(' Тип: ', '').strip() == 'TV Сериал':
                release_date = soup.find_all('div', class_='line-container')[3].get_text().replace('  Статус:  ',
                                                                                                   '').strip().capitalize()
                num_of_episodes = soup.find_all('div', class_='line-container')[1].get_text().replace('Эпизоды: ',
                                                                                                      '').strip()
            else:
                release_date = soup.find_all('div', class_='line-container')[2].get_text().replace('  Статус:  ',
                                                                                                   '').strip().capitalize()
                num_of_episodes = '1'
            pub_date = datetime.datetime.now()
            data_of_title = {
                'name_ru': name_ru,
                'name_eng': name_eng,
                'rating': rating,
                'genre': genres_list,
                'status': status,
                'release_date': release_date,
                "num_of_episodes": num_of_episodes,
                "pub_date": pub_date,
            }
            data.update({str(i): data_of_title})
            # print(data_of_title)
            print(data)
            i += 1
            time.sleep(1.5)
        return data

    def parce(self):
        html = self.get_html()
        if html.status_code == 200:
            predata = self.get_content(html.text)
            data = self.get_data(predata)
            # print(data)
            return data
        else:
            print('нет доступа к странице!')
            print(html.status_code)


Parce = Parce(url, headers)
data = Parce.parce()
print(data)


def add_titles_in_script(data):
    conn = psycopg2.connect(host="", database="ken", user="ken", password="zxcqwe123")
    cursor = conn.cursor()
    for value in data:
        name_ru = data[value]['name_ru']
        # genre = data[value]['genre']
        release_date = data[value]['release_date']
        num_of_episodes = data[value]['num_of_episodes']
        pub_date = data[value]['pub_date']
        name_eng = data[value]['name_eng']
        rating = data[value]['rating']
        status = data[value]['status']
        extent = '5'
        cursor.execute("""INSERT INTO catalog_anime_title
            (name_ru, release_date, num_of_episodes, pub_date, name_eng, rating, status, extent)
            VALUES (%s, %s, %s, %s, %s,%s, %s, %s)""",
                       (name_ru, release_date, num_of_episodes, pub_date, name_eng, rating, status, extent))
    conn.commit()
    cursor.close()
    conn.close()


add_titles_in_script(data)

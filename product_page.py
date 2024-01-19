import requests
from bs4 import BeautifulSoup


class Additional:

    def get_product_characteristic(self, link):
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")
        try:
            section = soup.find("div", class_="configuration")
            items = section.find_all("div", class_="configuration-item")
            characteristics = {}
            for item in items:
                details = item.find("div", class_="configuration-item-row-detail")
                title = details.find("span", class_="title").get_text()
                info = details.find("span", class_="info").get_text(strip=True)
                characteristics.update({title: info})
        except:
            characteristics = {"info": "Нет информации"}
        finally:
            return characteristics

    def get_product_desc(self, link):
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, "html.parser")
        try:
            info_product = soup.find("div", class_="info-producct")
            description = info_product.find("div", class_="detail__info-card").get_text()
            return description
        except:
            return "Нет информации !"
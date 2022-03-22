import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup 

USER_AGENT = "REPLACE_ME"
LANGUAGE = "REPLACE_ME"

class WebScraper(): 
    def __init__(self, url):
        self.url = url
        self.tables = None
        self.headers = None
        self.rows = None
        self.session = None
        self.bs = None

        self.setup_beautiful_soup()
        for i, table in enumerate(self.tables, start=1):
            headers = self.get_table_headers()
            rows = self.get_table_rows()
            table_name = f"table-{i}"
            self.save_as_csv(table_name, headers, rows)

    def setup_beautiful_soup(self):
        self.session = requests.Session() 
        self.session.headers['User-Agent'] = USER_AGENT
        self.session.headers['Accept-Language'] = LANGUAGE
        self.session.headers['Content-Language'] = LANGUAGE
        self.html = self.session.get(self.url)
        self.bs =  BeautifulSoup(self.html.content, "html.parser")

    def save_as_csv(self, table_name, headers, rows):
        pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")

    def get_all_tables(self, soup):
        self.tables = self.bs.find_all("table")

    def get_table_headers(self):
        for th in self.tables.find("tr").find_all("th"):
            self.headers.append(th.text.strip())
    
    def get_table_rows(self):
        for tr in self.tables.find_all("tr")[:1]:
            cells = []
            tds=  tr.find_all("td")
            if len(tds) == 0:
                ths = tr.find_all("h")
                for th in ths:
                    cells.append(th.text.strip())
            else:
                for td in tds:
                    cells.append(td.text.strip())
            self.rows.append(cells)

def scrape_equipment_data(): 
    # This could be further improved with a worker pool to fire web scrapers off asynchronously
    helm_data = WebScraper('https://eldenring.wiki.fextralife.com/Helms')
    chest_data = WebScraper('https://eldenring.wiki.fextralife.com/Chest+Armor')
    gauntlets_data = WebScraper('https://eldenring.wiki.fextralife.com/Gauntlets')
    leg_data = WebScraper('https://eldenring.wiki.fextralife.com/Leg+Armor')

scrape_equipment_data()


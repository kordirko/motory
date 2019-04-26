import scrapy

STRONA_GLOWNA = 'https://www.otomoto.pl/motocykle-i-quady/'
XPATH_DO_OFERT="//*[@class='offers list']/article//a[@class='offer-title__link']"

# scrapy crawl motory -o motory.json

class MotorySpider(scrapy.Spider):
    name = "motory"

    def start_requests(self):
        return [scrapy.Request(STRONA_GLOWNA, self.parse_strona_glowna)]

    def parse_strona_glowna(self, response):
        # na głównej stronie zbadaj jaka jest liczba stron
        lista_numerow_stron = response.xpath('//li//span[@class="page"]/text()')
        ostatnia_strona = lista_numerow_stron[-1].get()

        # generuj strony z listą ofert do dalszej analizy i parsowania
        for x in range(1,int(ostatnia_strona)+1):
            url = STRONA_GLOWNA + '?page=' + str(x)
            yield scrapy.Request(url, self.parse_podstrona)

    def parse_podstrona(self, response):
        oferty = response.xpath(XPATH_DO_OFERT)

        for oferta in oferty:
            link_do_oferty = oferta.attrib['href']
            print(link_do_oferty)
            yield scrapy.Request(link_do_oferty, self.parse_oferta)
# response.xpath('//*[@class="offer-params"]')

    def parse_oferta(selfself, response):
        pola_oferty = {}
        parametry_oferty = response.xpath('//*[@class="offer-params"]//li[@class="offer-params__item"]')
        for parametr in parametry_oferty:
            nazwa_pola = parametr.xpath('.//*[@class="offer-params__label"]/text()').get()
            # wartosc jest albo w zagnieżdżonym tagu A, albo bezpośrednio w tagu DIV
            wartosc_pola = parametr.xpath('.//*[@class="offer-params__value"]/a/text()').get()
            if wartosc_pola == None:
                wartosc_pola = parametr.xpath('.//*[@class="offer-params__value"]/text()').get()
            wartosc_pola = wartosc_pola.strip()
            pola_oferty[nazwa_pola] = wartosc_pola
        #jeszcze lokalizacja, cena, waluta i link - są w oddzielnych sekcjach
        lokalizacja = response.xpath('//*[@class="offer-content__main-column"]//*[@class="seller-box__seller-address__label"]/text()').get().strip()
        cena = response.xpath('//*[@class="offer-price__number"]/text()').get().strip().replace(" ", "")
        waluta = response.xpath('//*[@class="offer-price__currency"]/text()').get().strip()
        pola_oferty["Lokalizacja"] = lokalizacja
        pola_oferty["Link"] = response.url
        pola_oferty["Cena"] = cena
        pola_oferty["Waluta"] = waluta
        yield pola_oferty
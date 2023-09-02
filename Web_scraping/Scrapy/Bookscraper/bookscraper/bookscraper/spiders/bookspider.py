import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.con"]
    start_urls = ["http://books.toscrape.con/"]

    def parse(self, response):
        pass

import scrapy

class MainOLX(scrapy.spider):
    name = "TesteOLX"

    start_urls = ['www.olx.com.br']

    def parse(self, response):
        self.log(f"Estou em: {response.url}")

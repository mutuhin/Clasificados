import scrapy

class ClassifiedSpider(scrapy.Spider):
    name = "classified_spider"
    base_url = "https://www.clasificadosonline.com/m/dmcListingm.asp?SecID=PR&keyword=&x=9&y="
    start_y = 8  
    end_y = 20  

    def start_requests(self):
        for y in range(self.start_y, self.end_y + 1):
            url = f"{self.base_url}{y}"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        listings = response.xpath("//td[@class='Ver14'][1]/font/a/@href").getall()
        print(listings)


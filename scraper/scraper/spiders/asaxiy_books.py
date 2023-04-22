import scrapy
import datetime


class AsaxiyBooksSpider(scrapy.Spider):
    name = 'asaxiy-books'
    start_urls = ['https://asaxiy.uz/uz/product/knigi?size=96']
    page_no = 0

    def parse(self, response, **kwargs):
        news_links = response.css('div.product__item.d-flex.flex-column.justify-content-between a::attr(href)').getall()
        yield from response.follow_all(news_links, self.parse_page)

        self.page_no += 1
        yield from response.follow_all([f'https://asaxiy.uz/uz/product/knigi/page={self.page_no}?size=96'], self.parse)
    
    def parse_page(self, response):
        yield {
            'title': response.css('h1.product-title::text').get(),
            #'body': ' '.join(response.css('div.content_text p::text').getall()),
            #'category': "Vazirlik yangiliklari",
            #'creation_data' : response.css('div.date_box::text').get(),
            'access_data' : datetime.datetime.now()
        }
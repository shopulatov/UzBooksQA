import scrapy
import datetime
from scraper.article_item import Article
from scraper.article_loader import ArticleLoader
from scraper.spiders.helpers import xpath_text_blocks


class AsaxiyBooksSpider(scrapy.Spider):
    name = 'asaxiy-books'
    start_urls = ['https://asaxiy.uz/uz/product/knigi/yazik=na-uzbekskom,uzb-rus?size=96']
    page_no = 0

    def parse(self, response, **kwargs):
        book_links = response.css('div.product__item.d-flex.flex-column.justify-content-between a::attr(href)').getall()
        links=[link for link in book_links if 'one-click' not in link and '#' not in link]
        yield from response.follow_all(links, self.parse_page)

        while self.page_no<33:
            self.page_no += 1
            yield from response.follow_all([f'https://asaxiy.uz/uz/product/knigi/yazik=na-uzbekskom,uzb-rus/page={self.page_no}?size=96'], self.parse)
    
    def parse_page(self, response):
        a = ArticleLoader(item=Article(), response=response)
        a.add_value('url', response.url)
        a.add_css('name', 'h1.product-title::text')
        a.add_xpath('description', f'//div[contains(@class, "description__item")]/{xpath_text_blocks()}')

        table_rows = response.xpath('//table[@class="table table-striped table-borderless"]/tbody/tr')
        table_data = {}
        for row in table_rows:
            key = row.xpath('td[@class="text-left"]/text()').get().strip()
            value = row.xpath('td[@class="text-right"]/text()').get().strip()
            table_data[key] = value

        a.add_value('isbn', table_data.get('ISBN', ''))
        a.add_value('num_pages', table_data.get('Betlar soni', ''))
        a.add_value('cover', table_data.get('Muqovasi', ''))
        a.add_value('year_published', table_data.get('Chop etilgan yili', ''))
        yield a.load_item()
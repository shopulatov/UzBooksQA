import scrapy

class Article(scrapy.Item):
    url=scrapy.Field()
    name=scrapy.Field()
    description=scrapy.Field()
    author=scrapy.Field(default='asaxiy.uz')

    isbn=scrapy.Field()
    num_pages=scrapy.Field()
    cover=scrapy.Field()
    year_published=scrapy.Field()
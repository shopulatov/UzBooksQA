from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader
from scraper.article_preprocessors import parse_uzbek_date, strip_punctuation, to_title_case, parse_date_to_format
from w3lib.html import remove_tags


class ArticleLoader(ItemLoader):
    """A custom Scrapy ItemLoader for loading information about an article."""

    default_output_processor = TakeFirst()

    name_in = MapCompose(remove_tags, str.strip)
    name_out = TakeFirst()

    description_in = MapCompose(remove_tags, str.strip)
    description_out = Join('\n')

    author_in = MapCompose(str.strip, strip_punctuation, to_title_case)
    author_out = Join("|")
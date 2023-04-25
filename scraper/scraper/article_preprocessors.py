import string
from datetime import datetime
import dateparser


def trim_punctuation_whitespace(s: str) -> str:
    # Create a translator object to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Use the translator
    s = s.translate(translator)

    # Remove whitespace
    s = s.strip()

    return s


def strip_punctuation(s: str) -> str:
    # Create a string of punctuation characters
    punctuation = string.punctuation

    # Use the strip() method to remove leading and trailing punctuation
    return s.strip(punctuation)


def to_title_case(s: str) -> str:
    # Split the string into a list of words
    words = s.split()

    # Iterate over the words and convert them to title case
    for i, word in enumerate(words):
        words[i] = word.title()

    # Join the words back into a single string
    return " ".join(words)


def parse_uzbek_date(date_str: str):
    # Parses all date formats, including Uzbek
    return dateparser.parse(date_str)


def parse_date_to_format(date_str: datetime):
    # Parse the datetime to the required format
    return date_str.strftime("%Y-%m-%d")
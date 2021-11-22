from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_version():
    assert __version__ == '0.1.0'


def test_get_citations_needed_count():
    count1 = get_citations_needed_count(
        'https://en.wikipedia.org/wiki/History_of_chocolate')
    count2 = get_citations_needed_count(
        'https://en.wikipedia.org/wiki/History_of_Mexico')
    count3 = get_citations_needed_count(
        'https://en.wikipedia.org/wiki/History_of_Jordan')
    assert count1 == 2
    assert count2 == 5
    assert count3 == 4

import argparse
import logging
logging.basicConfig(level=logging.INFO)
import re

import news_page_objects as news
from common import config

logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^https://.+/.+$') #https://example.com/hello

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, host, link)

def _fetch_article(news_site_uid, host, link):
    logger.info('Start fetching article at {}'.format(link))

    article = None
    try:
        article = news.ArticlePage(news_site_uid, _build_link(host, link))
    except:
        pass

def _build_link(host, link):


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_site_choices)
    
    args = parser.parse_args()
    _news_scraper(args.news_site)

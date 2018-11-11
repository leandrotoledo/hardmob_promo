#!/usr/bin/env python
from os import environ
from bs4 import BeautifulSoup
import cfscrape


class Posts(object):

    @staticmethod
    def fetch():
        url = environ.get('URL')
        scraper = cfscrape.create_scraper()
        html = scraper.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        posts = list()

        for link in soup.select('#threads a.title'):
            post = dict()

            try:
                post['title'] = link.text
                post['href'] = link.get('href')
                post['uid'] = int(post['href'].replace(url, '')[:6])  # TODO

                posts.append(post)
            except Exception as e:
                print(e)

                pass

        return posts

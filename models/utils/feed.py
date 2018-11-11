#!/usr/bin/env python
from os import environ
from bs4 import BeautifulSoup
import cfscrape


class Posts(object):

    @staticmethod
    def fetch():
        url = environ.get('URL')
        root_url = environ.get('ROOT_URL')

        scraper = cfscrape.create_scraper()
        html = scraper.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        posts = list()

        for link in soup.select('#threads a.title'):
            post = dict()

            try:
                post['title'] = link.text
                post['href'] = root_url + link.get('href')
                post['uid'] = post['href'].replace(root_url + 'threads/', '')[:6] #TODO

                posts.append(post)
            except Exception as e:
                print(e)

                pass

        return posts

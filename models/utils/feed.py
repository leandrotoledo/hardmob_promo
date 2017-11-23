#!/usr/bin/env python
from os import environ
from bs4 import BeautifulSoup
import requests


class Posts(object):

    @staticmethod
    def fetch():
        url = environ.get('URL')
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        posts = list()

        for link in soup.select('#threads a.title'):
            post = dict()

            post['title'] = link.text
            post['href'] = link.get('href')
            post['uid'] = int(post['href'].replace(url, '')[:6])  # TODO

            posts.append(post)

        return posts

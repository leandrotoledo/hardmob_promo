#!/usr/bin/env python
from datetime import datetime
from pony.orm import *

from . import db
from .utils import Posts

import html


class Post(db.Entity):

    uid = Required(int, unique=True)
    title = Required(str)
    href = Required(str)

    created_at = Required(datetime, default=datetime.now)
    is_sent = Required(bool, default=False)
    sent_at = Optional(datetime)

    def text(self):
        return '<a href="%s">%s</a>' % (self.href, html.escape(self.title))


@db_session
def updatedb():
    for post in Posts.fetch():
        if not select(p for p in Post if p.uid == post['uid']):
            Post(**post)


@db_session
def get_posts(limit=0, sent_only=False):
    posts = select(p for p in Post if p.is_sent == sent_only) \
        .order_by(desc(Post.uid))

    if limit:
        return posts[:limit]

    return posts[:]


@db_session
def mark_as_sent(post_uid):
    post = Post.get(uid=post_uid)

    if post:
        post.is_sent = True
        post.sent_at = datetime.now()

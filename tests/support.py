from genrss import GenRSS


def create_rss(**kwargs):
    return GenRSS(title='SmartFridge', site_url='https://smartfridge.me/',
                  feed_url='https://smartfridge.me/rss.xml', **kwargs)


def create_item(feed, **kwargs):
    feed.item(title='Recipe', **kwargs)

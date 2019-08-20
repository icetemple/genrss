from uuid import uuid4
from datetime import datetime

import pytz
import pytest
from genrss import Enclosure
from tests.support import create_rss, create_item


@pytest.fixture()
def feed():
    return create_rss()


def test_item(feed):
    create_item(feed)
    xml = feed.xml()
    assert xml
    assert '<item><title><![CDATA[Recipe]]></title>' \
           '<description><![CDATA[]]></description>' \
           '<guid isPermaLink="false"><![CDATA[Recipe]]></guid>' \
           '</item>' in xml


def test_item_description(feed):
    description = 'description'
    create_item(feed, description=description)
    xml = feed.xml()
    assert xml
    assert '<item><title><![CDATA[Recipe]]></title>' \
           '<description><![CDATA[{}]]></description>' \
           '<guid isPermaLink="false"><![CDATA[Recipe]]></guid>' \
           '</item>'.format(description) in xml


def test_item_guid(feed):
    guid = uuid4().hex
    create_item(feed, guid=guid)
    xml = feed.xml()
    assert xml
    assert '<item><title><![CDATA[Recipe]]></title>' \
           '<description><![CDATA[]]></description>' \
           '<guid isPermaLink="false">{}</guid>' \
           '</item>'.format(guid) in xml


def test_item_url(feed):
    url = 'https://smartfridge.me/'
    create_item(feed, url=url)
    xml = feed.xml()
    assert xml
    assert '<item><title><![CDATA[Recipe]]></title>' \
           '<description><![CDATA[]]></description>' \
           '<link>{url}</link>' \
           '<guid isPermaLink="true">{url}</guid>' \
           '</item>'.format(url=url) in xml


def test_item_author(feed):
    author = 'Dmitriy Pleshevskiy'
    create_item(feed, author=author)
    create_item(feed, author=author)
    xml = feed.xml()
    assert xml
    assert '<dc:creator><![CDATA[{}]]></dc:creator>' \
           '</item>'.format(author) in xml


def test_item_categories(feed):
    categories = ['Category 1', 'Category 2']
    create_item(feed, categories=categories)
    xml = feed.xml()
    assert xml
    assert '<category><![CDATA[Category 1]]></category>' \
           '<category><![CDATA[Category 2]]></category>' \
           '</item>' in xml


def test_item_pub_date(feed):
    pub_date = datetime.utcnow()
    expose = pub_date.replace(tzinfo=pytz.timezone('GMT')). \
        strftime("%a, %d %b %Y %H:%M:%S %Z")
    create_item(feed, pub_date=pub_date)
    xml = feed.xml()
    assert xml
    assert '<pubDate>{}</pubDate>' \
           '</item>'.format(expose) in xml


def test_item_enclosure(feed):
    enclosure=Enclosure('https://smartfridge.me/image.jpg')
    create_item(feed, enclosure=enclosure)
    xml = feed.xml()
    assert xml
    assert '<enclosure url="{url}" length="{length}" type="{type}"/>' \
           '</item>'.format(length=0, type='image/jpeg',
                            url=enclosure.url) in xml


def test_item_enclosure_from_dict(feed, enclosure_dict):
    create_item(feed, enclosure=enclosure_dict)
    xml = feed.xml()
    assert xml
    assert '<enclosure url="{url}" length="{length}" type="{type}"/>' \
           '</item>'.format(length=enclosure_dict.get('size', 0),
                            type=enclosure_dict.get('type', 'image/jpeg'),
                            url=enclosure_dict.get('url')) in xml

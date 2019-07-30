from datetime import datetime
from textwrap import dedent

import pytz
import pytest
from genrss import RSS_DEFAULT_GENERATOR, Item
from tests.support import create_rss


def test_init_rss():
    feed = create_rss()
    xml = feed.xml()
    assert xml
    assert '<title><![CDATA[SmartFridge]]></title>' in xml
    assert '<description><![CDATA[SmartFridge]]></description>' in xml
    assert '<link>https://smartfridge.me/</link>' in xml
    assert '<atom:link href="https://smartfridge.me/rss.xml" rel="self" ' \
           'type="application/rss+xml"/>' in xml
    assert '<generator>{}</generator>'.format(RSS_DEFAULT_GENERATOR) in xml


@pytest.mark.parametrize('description, expose', [
    pytest.param('a' * 10, 'a' * 10, id='short(10)'),
    pytest.param('a' * 285, 'a' * 285, id='long(285)'),
    pytest.param(
        dedent('''\
        This is text with 
        new lines.'''),
        dedent('''\
        This is text with 
        new lines.'''),
        id='+nl'
    )
])
def test_feed_description(description, expose):
    feed = create_rss(description=description)
    xml = feed.xml()
    assert xml
    assert '<description><![CDATA[{}]]></description>'.format(expose) in xml


@pytest.mark.parametrize('copyright, expose', [
    pytest.param('copyright © genrss', 'copyright © genrss', id='copy'),
])
def test_feed_copyright(copyright, expose):
    feed = create_rss(copyright=copyright)
    xml = feed.xml()
    assert xml
    assert '<copyright><![CDATA[{}]]></copyright>'.format(expose) in xml


def test_feed_pub_date():
    pub_date = datetime.utcnow()
    feed = create_rss(pub_date=pub_date)
    xml = feed.xml()
    expose = pub_date.replace(tzinfo=pytz.timezone('GMT')). \
        strftime("%a, %d %b %Y %H:%M:%S %Z")
    assert xml
    assert '<pubDate>{}</pubDate>'.format(expose) in xml


def test_feed_language():
    lang = 'en'
    feed = create_rss(language=lang)
    xml = feed.xml()
    assert xml
    assert '<language><![CDATA[{}]]></language>'.format(lang) in xml


def test_feed_editor():
    editor = 'Dmitriy Pleshevskiy'
    feed = create_rss(editor=editor)
    xml = feed.xml()
    assert xml
    assert ('<managingEditor><![CDATA[{}]]>'
            '</managingEditor>').format(editor) in xml


def test_feed_image_url():
    image_url = 'https://s3.smartfridge.me/image.jpg'
    feed = create_rss(image_url=image_url)
    xml = feed.xml()
    assert xml
    assert (f'<image><url>{image_url}</url>'
            '<title><![CDATA[SmartFridge]]></title>'
            '<link>https://smartfridge.me/</link></image>') in xml


def test_feed_webmaster():
    webmaster = 'Dmitriy Pleshevskiy'
    feed = create_rss(webmaster=webmaster)
    xml = feed.xml()
    assert xml
    assert '<webMaster><![CDATA[{}]]></webMaster>'.format(webmaster) in xml


def test_feed_docs_url():
    docs_url = 'https://smartfridge.me/docs'
    feed = create_rss(docs_url=docs_url)
    xml = feed.xml()
    assert xml
    assert '<docs>{}</docs>'.format(docs_url) in xml


def test_feed_categories():
    categories = ['Category 1', 'Category 2']
    feed = create_rss(categories=categories)
    xml = feed.xml()
    assert xml
    assert '<category><![CDATA[Category 1]]></category>' \
           '<category><![CDATA[Category 2]]></category>' in xml


def test_feed_bad_items():
    feed = create_rss(items=['item'])
    xml = feed.xml()
    assert xml
    assert '<item>' not in xml


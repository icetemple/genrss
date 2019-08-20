from datetime import datetime
from typing import Optional, List, Dict

from lxml.etree import Element, CDATA, tostring

from .utils import create_element, ElementT
from .item import Item
from .enclosure import Enclosure

__all__ = ('GenRSS', 'Item', 'Enclosure')


RSS_DEFAULT_GENERATOR = f'Generated by genrss for python'


class GenRSS:
    """Generates RSS feed of channel.

    :param title: Title of your site or feed
    :param site_url: Absolute url to the site that the feed is for
    :param feed_url: Absolute url to the rss feed
    :param description: A short description of feed
    :param image_url: Image absolute url for channel
    :param author: Author of channel
    :param pub_date: Datetime in utc when last item was published
    :param copyright: Copyright information for this feed
    :param language: The language of the content of this feed.
    :param editor: Who manages content in this feed
    :param webmaster: Who manages feed availability and technical support
    :param generator: Feed generator
    """

    def __init__(self, title: str, site_url: str, feed_url: str, **kwargs):
        self.title: str = title
        self.site_url: str = site_url
        self.feed_url: str = feed_url
        self.description: str = kwargs.pop('description', self.title)
        self.image_url: Optional[str] = kwargs.pop('image_url', None)
        self.author: Optional[str] = kwargs.pop('author', None)
        self.pub_date: Optional[datetime] = kwargs.pop('pub_date', None)
        self.copyright: Optional[str] = kwargs.pop('copyright', None)
        self.language: Optional[str] = kwargs.pop('language', None)
        self.editor: Optional[str] = kwargs.pop('editor', None)
        self.webmaster: Optional[str] = kwargs.pop('webmaster', None)
        self.docs_url: Optional[str] = kwargs.pop('docs_url', None)
        self.categories: List[str] = kwargs.pop('categories', [])

        self.items: List[Item] = kwargs.pop('items', [])
        self.generator: str = kwargs.pop('generator', RSS_DEFAULT_GENERATOR)
        self.root_version: str = '2.0'
        self.root_nsmap: Dict[str, str] = {
            'atom': 'http://www.w3.org/2005/Atom',
            'dc': 'http://purl.org/dc/elements/1.1/'
        }

    def item(self, title: str, **kwargs):
        """Adds item to the feed.

        An item can be used for recipes, blog entries, project update, log
        entry, etc. Your RSS feed can have any number of items.

        :param title: Title of this particular item
        :param description: Content for the item. Can contain html but
            link and image urls must be absolute path including hostname
        :param url: Url to the item. This could be a blog entry
        :param guid: A unique string feed readers use to know if an item
            is new or has already been seen. If you use a guid never change
            it. If you don't provide a guid then your item urls must be unique
        :param author: If included it is the name of the item's creator.
            If not provided the item author will be the same as the feed
            author. This is typical except on multi-author blogs
        :param categories: If provided, each array item will be added as a
            category element
        :param enclosure: An enclosure object
        :param pub_date: The date and time of when the item was created.
            Feed readers use this to determine the sort order. Some readers
            will also use it to determine if the content should be presented
            as unread
        """
        self.items.append(Item(title, **kwargs))

    def to_element(self) -> ElementT:
        """Returns root element for xml."""
        root = Element('rss', nsmap=self.root_nsmap, version=self.root_version)
        channel = create_element('channel', children=[
            create_element('title', CDATA(self.title)),
            create_element('description', CDATA(self.description)),
            create_element('link', self.site_url),
            create_element('{http://www.w3.org/2005/Atom}link',
                           href=self.feed_url, rel='self',
                           type='application/rss+xml'),
            create_element('generator', self.generator),
            create_element('lastBuildDate', datetime.utcnow())
        ])

        if self.image_url:
            channel.append(create_element('image', children=[
                create_element('url', self.image_url),
                create_element('title', CDATA(self.title)),
                create_element('link', self.site_url)
            ]))
        for category in self.categories:
            channel.append(create_element('category', CDATA(category)))
        if self.pub_date:
            channel.append(create_element('pubDate', self.pub_date))
        if self.copyright:
            channel.append(create_element('copyright', CDATA(self.copyright)))
        if self.language:
            channel.append(create_element('language', CDATA(self.language)))
        if self.editor:
            channel.append(create_element('managingEditor', CDATA(self.editor)))
        if self.webmaster:
            channel.append(create_element('webMaster', CDATA(self.webmaster)))
        if self.docs_url:
            channel.append(create_element('docs', self.docs_url))

        for item in self.items:
            if isinstance(item, Item):
                channel.append(item.to_element())

        root.append(channel)
        return root

    def xml(self, pretty: bool = False) -> str:
        """Returns the XML as a string.

        :param pretty: Pretty print xml
        """
        root = self.to_element()

        return tostring(root, pretty_print=pretty, xml_declaration=True,
                        encoding='UTF-8'). \
            decode('utf-8')

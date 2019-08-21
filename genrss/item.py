from datetime import datetime
from typing import Optional, List, Union, Dict

from lxml.etree import CDATA

from .utils import ElementT, create_element
from .enclosure import Enclosure, EnclosureOrDictT
from .image import Image

__all__ = ('Item',)


class Item:
    """Data for item tag for rss.

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
    :param image: An image object
    :param pub_date: The date and time of when the item was created.
        Feed readers use this to determine the sort order. Some readers
        will also use it to determine if the content should be presented
        as unread
    """

    def __init__(self, title: str, **kwargs):
        self.title: str = title
        self.description: str = kwargs.pop('description', '')
        self.url: Optional[str] = kwargs.pop('url', None)
        self.guid: Optional[str] = kwargs.pop('guid', None)
        self.author: Optional[str] = kwargs.pop('author', None)
        self.categories: List[str] = kwargs.pop('categories', [])
        self.enclosure: Optional[Enclosure, Dict] = kwargs.pop('enclosure',
                                                               None)
        self.image: Optional[Image, Dict] = kwargs.pop('image', None)
        self.pub_date: Optional[datetime] = kwargs.pop('pub_date', None)

        if isinstance(self.enclosure, dict):
            self.enclosure = Enclosure.from_dict(self.enclosure)
        if isinstance(self.image, dict):
            self.image = Image.from_dict(self.image)

    def to_element(self) -> ElementT:
        """Returns item element for xml."""
        item = create_element('item', children=[
            create_element('title', CDATA(self.title)),
            create_element('description', CDATA(self.description)),
        ])

        if self.url:
            item.append(create_element('link', self.url))

        item.append(create_element(
            'guid',
            attrib={
                'isPermaLink': str(bool(not self.guid and self.url)).lower()
            },
            text=(self.guid or self.url or CDATA(self.title))
        ))

        if self.author:
            item.append(create_element(
                '{http://purl.org/dc/elements/1.1/}creator',
                CDATA(self.author)
            ))

        for category in self.categories:
            item.append(create_element('category', CDATA(category)))
        if self.enclosure:
            item.append(self.enclosure.to_element())
        if self.pub_date:
            item.append(create_element('pubDate', self.pub_date))

        return item

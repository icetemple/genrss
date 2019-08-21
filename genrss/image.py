from typing import Dict, Union
from lxml.etree import CDATA

from .utils import ElementT, create_element

__all__ = ('Image',)


class Image:
    """The element allows an image to be displayed when aggregators
    present a feed.

    :param url: Absolute url to the image
    :param link: Hyperlink to the website
    :param title: Text to display if the image could not be shown
    :param description: Specifies the text in the HTML title attribute of the
        link around the image
    :param width: The width of the image
    :param height: The height of the image
    """

    def __init__(self, url: str, link: str, title: str, description: str = None,
                 width: int = None, height: int = None):
        self.url = url
        self.link = link
        self.title = title
        self.description = description
        self.height = height
        self.width = width

    def to_element(self) -> ElementT:
        """Returns image element for xml."""
        image = create_element('image', children=[
            create_element('url', self.url),
            create_element('link', self.link),
            create_element('title', CDATA(self.title))
        ])

        if self.description:
            image.append(create_element('description', CDATA(self.description)))
        if self.height:
            image.append(create_element('height', self.height))
        if self.width:
            image.append(create_element('width', self.width))

        return image

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int]]):
        """Makes image data from dict."""
        return cls(**data)

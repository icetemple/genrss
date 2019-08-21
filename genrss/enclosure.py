import mimetypes
from typing import Dict, Union, TypeVar, Dict

from .utils import ElementT, create_element

__all__ = ('Enclosure', 'EnclosureOrDictT')


class Enclosure:
    """Data for enclosure tag for rss.

    :param url: Absolute url to file
    :param size: File size
    :param type: File mime type
    """

    def __init__(self, url: str, size=None, type=None):
        self.url = url
        self.size = size or 0
        self.type = type or mimetypes.guess_type(self.url)[0]

    def to_element(self) -> ElementT:
        """Returns item element for xml."""
        return create_element('enclosure', url=self.url, length=str(self.size),
                              type=self.type)

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int]]):
        """Makes enclosure data from dict."""
        return cls(**data)


EnclosureOrDictT = Union[Enclosure, Dict]

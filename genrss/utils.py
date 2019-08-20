from datetime import datetime
from typing import TypeVar, Any, List

import pytz
from lxml.etree import Element

__all__ = ('ElementT', 'create_element',)


ElementT = TypeVar('ElementT')


def create_element(name: str, text: Any = None, children: List[ElementT] = None,
                   **kwargs) -> ElementT:
    """Creates xml node with text or children elements.

    :param name: Tag name of node with namespace
    :param text: Text of node
    :param children: Appends elements as child nodes
    """
    el = Element(name, **kwargs)
    if text:
        if isinstance(text, datetime):
            text = text.replace(tzinfo=pytz.timezone('GMT')). \
                strftime("%a, %d %b %Y %H:%M:%S %Z")
        el.text = text
    elif isinstance(children, (list, tuple)):
        for child in children:
            el.append(child)
    return el

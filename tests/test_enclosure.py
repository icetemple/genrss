import pytest
from genrss import Enclosure


def test_init_fails():
    with pytest.raises(TypeError):
        Enclosure()
        assert False


def test_init(enclosure_tuple):
    url, size, type = enclosure_tuple
    enclosure = Enclosure(url, size, type)
    assert enclosure.url == url
    assert enclosure.size == (size or 0)
    assert enclosure.type == (type or 'image/jpeg')


def test_init_from_dict(enclosure_dict):
    enclosure = Enclosure.from_dict(enclosure_dict)
    assert enclosure.url == enclosure_dict.get('url')
    assert enclosure.size == enclosure_dict.get('size', 0)
    assert enclosure.type == enclosure_dict.get('type', 'image/jpeg')

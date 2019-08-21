import pytest
from genrss import Image


def test_init_image_fails():
    with pytest.raises(TypeError):
        Image()
        assert False


def test_init_image(image_tuple):
    url, link, title, description, width, height = image_tuple
    image = Image(url, link, title, description, width, height)
    assert image.url == url
    assert image.link == link
    assert image.title == title
    assert image.description == description
    assert image.width == width
    assert image.height == height


def test_init_image_from_dict(image_dict):
    image = Image.from_dict(image_dict)
    assert image.url == image_dict.get('url')
    assert image.link == image_dict.get('link')
    assert image.title == image_dict.get('title')
    assert image.description == image_dict.get('description')
    assert image.width == image_dict.get('width')
    assert image.height == image_dict.get('height')

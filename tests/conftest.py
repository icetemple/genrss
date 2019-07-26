import pytest

IMAGE_URL = 'http://s3.smartfridge.me/image.jpg'


@pytest.fixture(params=[
    pytest.param((IMAGE_URL, None, None), id='+/-/-'),
    pytest.param((IMAGE_URL, 1000, None), id='+/+/-'),
    pytest.param((IMAGE_URL, 1000, 'image/png'), id='+/+/+'),
    pytest.param((IMAGE_URL, None, 'image/png'), id='+/-/+'),
])
def enclosure_tuple(request):
    return request.param


@pytest.fixture(params=[
    pytest.param(dict(url=IMAGE_URL), id='+/-/-'),
    pytest.param(dict(url=IMAGE_URL, size=1000), id='+/+/-'),
    pytest.param(dict(url=IMAGE_URL, size=1000, type='image/png'), id='+/+/+'),
    pytest.param(dict(url=IMAGE_URL, type='image/png'), id='+/-/+'),
])
def enclosure_dict(request):
    return request.param

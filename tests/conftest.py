import pytest

IMAGE_URL = 'https://s3.smartfridge.me/image.jpg'
SITE_URL = 'https://smartfridge.me/'
SITE_TITLE = 'Smart Fridge'

IMAGE_DESCRIPTION = 'a'*100
IMAGE_HEIGHT = 100
IMAGE_WIDTH = 100



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


@pytest.fixture(params=[
    pytest.param((None, None, None), id='-/-/-'),
    pytest.param((IMAGE_DESCRIPTION, None, None), id='+/-/-'),
    pytest.param((IMAGE_DESCRIPTION, 100, None), id='+/+/-'),
    pytest.param((IMAGE_DESCRIPTION, 100, 200), id='+/+/+'),
])
def image_tuple(request):
    return (IMAGE_URL, SITE_URL, SITE_TITLE) + request.param


@pytest.fixture(params=[
    pytest.param(dict(), id='-/-/-'),
    pytest.param(dict(description=IMAGE_DESCRIPTION), id='+/-/-'),
    pytest.param(dict(description=IMAGE_DESCRIPTION, width=100), id='+/+/-'),
    pytest.param(dict(description=IMAGE_DESCRIPTION, width=100, height=100),
                 id='+/+/+'),
])
def image_dict(request):
    return dict(
        url=IMAGE_URL,
        link=SITE_URL,
        title=SITE_TITLE,
        **request.param
    )

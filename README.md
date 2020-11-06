# genrss

[![PyPI version](https://badge.fury.io/py/genrss.svg)](https://badge.fury.io/py/genrss)
[![Build Status](https://travis-ci.org/icetemple/genrss.svg?branch=master)](https://travis-ci.org/icetemple/genrss)
[![Coverage Status](https://coveralls.io/repos/github/icetemple/genrss/badge.svg?branch=master)](https://coveralls.io/github/icetemple/genrss?branch=master)
[![Documentation Status](https://readthedocs.org/projects/genrss/badge/?version=latest)](https://genrss.readthedocs.io/en/latest/?badge=latest)

RSS generator for python


## Installing

genrss using lxml library that required:

* libxml2 version 2.9.2 or later.
* libxslt version 1.1.27 or later.

To install the required development packages of these dependencies on Linux systems,
use your distribution specific installation tool, e.g. apt-get on Debian/Ubuntu:

```bash
sudo apt-get install libxml2-dev libxslt-dev
```


Install and update using pip:

```bash
pip install -U genrss
```


## A Simple Example

```python
from datetime import datetime
from genrss import GenRSS

feed = GenRSS(title='SmartFridge',
              site_url='https://smartfridge.me',
              feed_url='https://smartfridge.me/feed/rss.xml')

feed.item(title='black buns for burgers',
          description='For the first time black burgers appeared ' \
                      'in Japan. Unusual dark color buns complemented ' \
                      'with black cheese and sauce. Over time, the dish ' \
                      'has conquered the whole world. The main secret ' \
                      'ingredient in popular buns is the most common... ' \
                      'charcoal!',
          url='https://smartfridge.me/recipe/316b28-chernye-bulochki-dlya-burgerov/',
          author='@smartfridge',
          categories=['baking'],
          pub_date=datetime.utcnow())

xml = feed.xml()
```

## Links

Documentation: [https://genrss.readthedocs.io/en/latest/](https://genrss.readthedocs.io/en/latest/)

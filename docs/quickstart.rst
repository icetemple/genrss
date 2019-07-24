.. _quickstart:

Quickstart
==========

Do you want to get started? This page gives a good introduction to GetRSS.
It assumes you already have GenRSS installed. If you do not, head over
to the :ref:`installation` section.


A Simple Example
----------------
.. code-block:: python

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

..

This code initializes small feed about recipe site with one item and returns
xml as string


For more information about GenRSS you can have a look :ref:`api` section.
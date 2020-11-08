.. _installation:

Installation
============

Python Version
--------------

We recommend using the latest version of Python 3. GenRSS supports
Python 3.6 and newer.


Dependencies
------------

genrss using lxml library that required:

* libxml2 version 2.9.2 or later.
* libxslt version 1.1.27 or later.

To install the required development packages of these dependencies on Linux systems,
use your distribution specific installation tool, e.g. apt-get on Debian/Ubuntu:

``sudo apt-get install libxml2-dev libxslt-dev``


Install GenRSS
--------------

Use the following command to install GenRSS:

``pip install -U genrss``

GenRSS is now installed. Check out :ref:`quickstart`

Install from source
-------------------

If you want to work with the latest GenRSS code before it’s released,
install or update the code from the master branch:

``pip install -U https://github.com/icetemple/genrss/archive/master.zip``

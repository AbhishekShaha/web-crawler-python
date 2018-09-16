<h1 align="center">web Crawler</h1>

<div align="center">
  :spider::spider::spider:
</div>
<div align="center">
  <strong>A simple web crawler using python</strong>
</div>
<br />

<div align="center">
  <!-- Stability -->
  <a href="https://nodejs.org/api/documentation.html#documentation_stability_index">
    <img src="https://img.shields.io/badge/stability-experimental-orange.svg?style=flat-square"
      alt="API stability" />
  </a>
  <!-- Build Status -->
  <a href="">
    <img src="https://img.shields.io/travis/choojs/choo/master.svg?style=flat-square"
      alt="Build Status" />
  </a>
  
  <!-- Platform -->
  <a href="">
    <img src="https://img.shields.io/badge/Python-2.7%7C3.5-green.svg"
      alt="Platform" />
  </a>
  <!-- Test Coverage -->
  <a href="o">
    <img src="https://img.shields.io/codecov/c/github/choojs/choo/master.svg?style=flat-square"
      alt="Test Coverage" />
  </a>
  <!-- Standard -->
  <a href="https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code">
    <img src="https://img.shields.io/badge/Code%20Style-PEP--8-blue.svg"
      alt="PEP-8" />
  </a>
</div>

<div align="center">
  <h3>
    <a href="https://abhishekshaha.github.io/">
      Website
    </a>
    <span> | </span>
    <a href="https://abhishekshaha.github.io/abhishekshaha.github.io/python/2018/09/16/blog-python.html">
      Blog
    </a>
  </h3>
</div>

<p align="center">
 <img src="https://user-images.githubusercontent.com/9308669/45591088-be34a700-b93f-11e8-8994-0701e44d9187.gif">
</p>

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#philosophy)
- [Credits](#support)

## Features

The most straightforward crawler that will crawl a site by bringing all the URL's for a particular given website.

## Requirements

- __BeautifulSoup:__ is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

- __Python2.7+__
- __And a terminal__

## Code Snippet

```python:
#!/usr/bin/python

#- * -coding: utf - 8 - * -

    inputURL = 'https://wiprodigital.com/'

# URL that we want to crawl

resultUrl = {
    inputURL: False
}

# Value is True or False.True means already crawled

# from urllib
import urlopen

import urllib2
import urlparse
import time
import pprint
import BeautifulSoup# get html links


def processOneUrl(url):
    ""
"fetch URL content and update resultUrl."
""

try: # in case of 404 error
html_page = urllib2.urlopen(url)
soup = BeautifulSoup.BeautifulSoup(html_page)
for link in soup.findAll('a'):
    fullurl = urlparse.urljoin(url, link.get('href'))
    if fullurl.startswith(inputURL):
        if fullurl not in resultUrl:
        resultUrl[fullurl] = False
    resultUrl[url] = True# set as crawled
    except:
        resultUrl[url] = True# set as crawled


    def moreToCrawl():
        ""
    "returns True or False"
    ""

    for (url, crawled) in iter(resultUrl.iteritems()):
        if not crawled:
        print 'The URL found is:  {}'.format(url)
    return url
    return False


    while True:
        toCrawl = moreToCrawl()
    if not toCrawl:
        break
    processOneUrl(toCrawl)
    time.sleep(2)

    pprint.pprint(resultUrl)
```

## Usage
```
$ python cr.py >> result.txt
```

### Credits
The code credit for this web crowler.
[Rishi Giri](https://opencollective.com/choo#backer)

## License
[MIT](https://tldrlegal.com/license/mit-license)


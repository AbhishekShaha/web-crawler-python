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

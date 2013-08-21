#!/usr/bin/env python

import re
import json
import time
import logging
import urlparse

import lxml.html
import requests

logging.basicConfig(filename="crawl.log", level=logging.INFO)
web = requests.Session()

def articles():
    for url in article_urls():
        yield get_article(url)

def get_article(url):
    doc = get(url)
    table = doc.xpath('.//table[@class="MPReader_Content_PrimitiveHeadingControl"]')[0]

    # title 
    title = table.xpath('./tr/td/h2/a')[0].text
    title = doc.xpath('.//title')[0].text.split("- American Archivist")[0].strip()


    tr = table.xpath('.//table/tr')

    # subject
    subject = [e.text for e in tr[3].xpath('.//a')]
    m = re.match('Volume (\d+), Number (\d+)', tr[4].xpath('.//a')[0].text)

    # volume
    volume, issue = m.groups()

    # pages
    pages = tr[6].xpath('td[@class="labelValue"]')[0].text

    # abstract
    e = doc.xpath('.//div[@class="abstract"]/p')
    if len(e) > 0:
        abstract = e[0].text
    else: 
        abstract = None

    # image 
    image = None
    pdf = None
    for a in doc.xpath('.//a'):
        href = a.attrib['href']
        if href and 'largest' in href:
            image = urlparse.urljoin(url, href)
        elif href and 'fulltext.pdf' in href:
            pdf = urlparse.urljoin(url, href)

    # author 
    div = doc.xpath('.//td[@class="mainPageContent"]/div')
    n = div[1].text.strip()
    if "," in n:
        names = [x.strip() for x in n.split(",")]
    else:
        names = [n.strip()]
    for e in div[1].xpath('./sup'):
        if e.tail:
            a = e.tail.strip()
            a = re.sub("^, ", "", a)
            author.append(a)

    # organization
    orgs = []
    p = doc.xpath('.//td[@class="mainPageContent"]/p')
    if len(p) > 0:
        for e in p[0].xpath('./sup'):
            if e.tail:
                orgs.append(e.tail.strip())

    author = []
    if len(names) == len(orgs):
        for i in range(0, len(names)):
            author.append({"name": names[i], "organization": orgs[i]})
    else:
        for i in range(0, len(names)):
            author.append({"name": names[i]})

    return {
        "subject": subject,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "title": title,
        "abstract": abstract,
        "url": url,
        "pdf": pdf,
        "image": image,
        "author": author,
    }

def article_urls():
    for issue_url in issue_urls():
        doc = get(issue_url)
        for div in doc.xpath('.//div[@class="primitiveControl"]'):
            a = div.xpath('./div[@class="listItemName"]/a')
            if len(a) > 0:
                yield urlparse.urljoin(issue_url, a[0].attrib['href'])

def issue_urls():
    url = "http://archivists.metapress.com/content/120809"
    while True:
        doc = get(url)
        for a in doc.xpath('.//a'):
            if a.text and a.text.startswith('Number'):
                yield urlparse.urljoin(url, a.attrib['href'])
            if a.text == "Next Page":
                next_page = urlparse.urljoin(url, a.attrib['href'])
        if next_page:
            url = next_page
            next_page = None
        else:
            break

def get(url):
    time.sleep(1)
    logging.info("getting %s", url)
    html = web.get(url, headers={"User-Agent": "americanarchivist: http://github.com/edsu/americanarchivist"}).content
    return lxml.html.fromstring(html)

def main():
    metadata = open("metadata.txt", "w")
    for article in articles():
        metadata.write(json.dumps(article))
        metadata.write("\n")

if __name__ == "__main__":
    main()

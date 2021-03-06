#!/usr/bin/env python

"""
Fetch article PDF and save to disk next to chunk of JSON about the article.
"""

import os
import re
import json
import time
import requests

articles = json.loads(open('../metadata.json').read())
for a in articles:
    slug = a["title"].lower()
    slug = re.sub("[^a-zA-Z0-9\s]", "", slug)
    slug = slug.replace(" ", "-")

    pdf_filename = "pdf/%s/%s/%s.pdf" % (a["volume"], a["issue"], slug)
    json_filename = "pdf/%s/%s/%s.json" % (a["volume"], a["issue"], slug)

    if os.path.isfile(pdf_filename):
        continue

    dir_name = os.path.dirname(pdf_filename)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    # last three volumes aren't available for free so don't store paywall html
    resp = requests.get(a["pdf"], verify=False)
    if resp.headers["content-type"] != "application/pdf":
        continue

    open(pdf_filename, "wb").write(resp.content)
    open(json_filename, "w").write(json.dumps(a, indent=2))
    print pdf_filename
    time.sleep(5)


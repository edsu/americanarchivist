#!/usr/bin/env python

import json

metadata = json.loads(open("../metadata.json").read())
for article in metadata:
    for author in article["author"]:
        print author["name"].encode('utf-8')


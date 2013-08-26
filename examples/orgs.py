#!/usr/bin/env python

import json

metadata = json.loads(open("../metadata.json").read())
for article in metadata:
    for author in article["author"]:
        if author.has_key("organization"):
            print author["organization"]


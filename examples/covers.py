#!/usr/bin/env python

import os
import json
import time

import requests

html = open("covers/index.html", "w")
html.write("""<!doctype html>
<html>
<head>
  <style>
    body {
    } 
    .cover {
      float: left;
      padding: 10px;
    }
    .cover img {
      height: 400px;
    }
  </style>
<body>
""")

for line in open("metadata.txt"):
    try:
        a = json.loads(line)
        if a["title"].startswith("Front Matter"):
            html.write('<div class="cover"><a href="%s"><img src="%02i-%02i.png"></a></div>\n' % (a["url"], int(a["volume"]), int(a["issue"])))
            filename = "covers/%02i-%02i.png" % (int(a["volume"]), int(a["issue"]))
            if os.path.isfile(filename):
                continue

            print filename
            open(filename, "w").write(requests.get(a["image"]).content)
            time.sleep(1)
    except ValueError:
        pass

html.write("</body>\n</html>")
html.close()

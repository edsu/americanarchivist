#!/usr/bin/env python

import csv
import json
import genderator.detector

detector = genderator.detector.Detector()
totals = [{0:0, 1:0, 2:0} for a in range(0, 76)]
metadata = json.loads(open("../metadata.json").read())

for article in metadata:
    for author in article["author"]:
        fn = author["name"].split(" ")[0]
        gender = detector.getGender(fn)
        volume = int(article["volume"]) - 1
        totals[volume][gender] = totals[volume].get(gender, 0) + 1

csvwriter = csv.writer(open("gender.csv", "w"))
for i in range(0, 76):
    row = totals[i]
    total = float(row[0] + row[1] + row[2])
    m = int(row[0] / total * 100)
    f = int(row[1] / total * 100)
    u = int(row[2] / total * 100)
    csvwriter.writerow([i + 1938, m, f, u])

    

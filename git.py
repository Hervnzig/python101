#!/usr/bin/python

import json
import datetime
import lxml
from lxml import etree
from lxml.etree import CDATA, tostring, fromstring

# Load json structured by an atavist report export

with open("data.json") as json_file:
    json_data = json.load(json_file)

    # Content Loop

    content = ""
    chapters = json_data["sections"]
    for x in xrange(len(chapters)):
        titles = "<h2>" + chapters[x]["title"] + "</h2>"
        content += titles
        content += (chapters[x]["body"])

    # Metadata
    meta = json_data["basics"]
    report_title = meta["title"]
    subtitle = meta["subtitle"]
    slug = meta["slug"]
    date = meta["pub_date"]

    # Convert UNIX timestamp to human-readable date

    h_date = datetime.datetime.fromtimestamp(
        int(date)).strftime('%Y-%m-%d %H:%M:%S')

    # Namespaces (Make this a valid RSS document)

    CNS = "http://purl.org/rss/1.0/modules/content/"
    WPNS = "http://wordpress.org/export/1.2/"
    NSMAP = {'content': "http://purl.org/rss/1.0/modules/content/",
             'wp': "http://wordpress.org/export/1.2/"}

    # XML Building

    rss = etree.Element('rss', nsmap=NSMAP, version="2.0")

    channel = etree.SubElement(rss, 'channel')
    item = etree.SubElement(channel, 'item')

    title = etree.SubElement(item, 'title')
    title.text = report_title

    link = etree.SubElement(item, 'link')
    link.text = slug

    pub_date = etree.SubElement(item, 'pubDate')
    pub_date.text = h_date

    wp_content = etree.SubElement(item, '{%s}encoded' % (CNS))
    wp_content.text = CDATA(content)
    tostring(wp_content, encoding="unicode")
    # print(tostring(wp_content, encoding="unicode"))

    wp_date = etree.SubElement(item, '{%s}post_date' % (WPNS))
    wp_date.text = CDATA(h_date)
    tostring(wp_date, encoding="unicode")

    # Serialize XML into single document with unicode encoding

    wp_import = tostring(rss, xml_declaration=True,
                         pretty_print=True, encoding="UTF-8")

# Write it to a file!

with open('wp_import_titles.xml', 'wb') as out:
    out.write(wp_import)

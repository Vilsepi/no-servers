#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from xml.etree import ElementTree
import json

# Import vendor modules from a subdirectory
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests
import boto3

# Download RSS Feed from Ampparit
def _get_feed_xml():
    url = "http://feeds.feedburner.com/ampparit-uutiset"
    response = requests.get(url)
    return response.content

# Parse news entries from RSS XML
def _parse_xml(xml):
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    id_prefix = "http://www.ampparit.com/redir.php?id="
    feed = ElementTree.fromstring(xml)
    parsed_entries = []
    for entry in feed.findall("atom:entry", ns):
        parsed_entries.append({
            "id": entry.find("atom:id", ns).text.split(id_prefix,1)[1],
            "title": entry.find("atom:title", ns).text,
            "updated": entry.find("atom:updated", ns).text,
            "url": entry.find("atom:link", ns).attrib.get("href"),
            "author": entry.find("atom:author", ns).find("atom:name", ns).text
        })
    print "Parsed {} items".format(len(parsed_entries))
    return parsed_entries

# Save entries to DynamoDB
def _save_to_dynamo(items):
    table_name = os.environ.get("TABLE_NAME")
    table = boto3.resource("dynamodb").Table(table_name)
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)

# Lambda entry point
def handler(event, context):
    items = _parse_xml(_get_feed_xml())
    if not event.get("is_local_dev"):
        _save_to_dynamo(items)
    else:
        print json.dumps(items, indent=1)
        raise NotImplementedError("Local DynamoDB usage not implemented")


# Main function for local testing
if __name__ == "__main__":
    print "Local execution is not completely supported. Please run this in AWS Lambda."
    handler({"is_local_dev": True}, {})

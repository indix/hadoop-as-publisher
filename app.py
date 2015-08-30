#!/usr/bin/env python

### Version - v1
# This script is supposed to be run from JT machine

import requests
import json
import boto
import socket
from BeautifulSoup import BeautifulSoup
from lib.Demand import *
from lib.Supply import *

HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]
JOB_TRACKER_URL = "http://" + HOSTNAME + ":50030/jobtracker.jsp"

config = json.load(open("config.json"))
METRIC_NAMESPACE = config['namespace']
METRIC_DIMENSION = config['dimensions']

response = requests.get(JOB_TRACKER_URL)
html = response.text
doc = BeautifulSoup(html)

supply = Supply(doc)
demand = Demand(doc)

# Send hadoop metrics
watch = boto.connect_cloudwatch()
watch.put_metric_data(METRIC_NAMESPACE, "nodes", supply.nodes(), dimensions = METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "map_supply", supply.map(), dimensions = METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "reduce_supply", supply.reduce(), dimensions = METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "map_demand", demand.map(), dimensions = METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "reduce_demand", demand.reduce(), dimensions = METRIC_DIMENSION)

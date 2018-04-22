#!/usr/bin/env python

### Version - v2
# This script is supposed to be run from Resource Manager machine

import requests
import json
import boto
import socket

if socket.getfqdn().find('.') >= 0:
    HOSTNAME= socket.getfqdn()
else:
    HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]
JOB_TRACKER_URL = "http://" + HOSTNAME + ":8088/ws/v1/cluster/metrics/"

config = json.load(open("config.json"))
METRIC_NAMESPACE = config['namespace']
METRIC_DIMENSION = config['dimensions']

response = requests.get(JOB_TRACKER_URL)
if (response.status_code == 200):
    yarn_cm = response.json()
else:
    print "Failed to fetch metrics, response.status_code %d" % response.status_code


containers_allocated = yarn_cm['clusterMetrics']['containersAllocated']
containers_pending = yarn_cm['clusterMetrics']['containersPending']
mem_allocated = max(yarn_cm['clusterMetrics']['allocatedMB'], 1)
total_memory = yarn_cm['clusterMetrics']['totalMB']
mem_health = total_memory / mem_allocated

unhealthy_nodes = yarn_cm['clusterMetrics']['unhealthyNodes']
active_nodes = yarn_cm['clusterMetrics']['activeNodes']

# Send YARN metrics
watch = boto.connect_cloudwatch()
watch.put_metric_data(METRIC_NAMESPACE, "active_nodes", active_nodes, dimensions = METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "containers_allocated", containers_allocated, dimensions=METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "containers_pending", containers_pending, dimensions=METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "mem_health", mem_health, dimensions = METRIC_DIMENSION)
watch.put_metric_data(METRIC_NAMESPACE, "unhealthy_nodes", unhealthy_nodes, dimensions = METRIC_DIMENSION)

# Hadoop Autoscaling Metric Publisher

## For YARN
We collect the following yarn metrics

- Active Nodes
- Containers Allocated
- Containers Pending
- Cluster Memory Usage
- Unhealthy Nodes
- Apps Running

## For Hadoop1

This is a simple python program that is expected to run on Cron on the JobTracker machine. We collect hadoop metrics like

- Total Map Slots
- Total Reduce Slots
- Total Nodes
- Number of Map slots Required
- Number of Reduce Slots Required

We push all these metrics to Cloudwatch periodcially. You can then create alarms which could trigger autoscaling of Hadoop Clusters. When visualized it as a Demand vs Supply it looks like this

![CloudWatch Dashboard](https://raw.githubusercontent.com/ashwanthkumar/hadoop-as-publisher/master/docs/cloudwatch-dashboard.png)

## License
Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0


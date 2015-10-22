# Hadoop Autoscaling Metric Publisher

This is a simple python program that is expected to run on Cron on the JobTracker machine. We collect hadoop metrics like

- Total Map Slots
- Total Reduce Slots
- Total Nodes
- Number of Map slots Required
- Number of Reduce Slots Required

We push all these metrics to Cloudwatch periodcially. You can then create alarms which could trigger autoscaling of Hadoop Clusters.

## Status
This is the bare bones implementation and should be considered alpha quality software.

## License
Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0


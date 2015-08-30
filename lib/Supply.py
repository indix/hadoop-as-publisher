import re

class Supply:

  def __init__(self, doc):
    self.cluster_summary = {}
    summary_table = doc.find("h2", text = re.compile("Cluster Summary")).parent.findNextSibling("table", {"border" : "1"})
    rows = summary_table.findAll('tr')
    for row in rows:
      cols = row.findAll('td')
      cols = [ele.text.strip() for ele in cols]
      cols = [ele for ele in cols if ele] # Get rid of empty values
      if len(cols) > 1:
        # Columns are
        # - Running Map Tasks
        # - Running Reduce Tasks
        # - Total Submissions
        # - Nodes
        # - Occupied Map Slots
        # - Occupied Reduce Slots
        # - Reserved Map Slots
        # - Reserved Reduce Slots
        # - Map Task Capacity
        # - Reduce Task Capacity
        # - Avg. Tasks/Node
        # - Blacklisted Nodes
        # - Excluded Nodes
        self.cluster_summary.update({
          'nodes' : int(cols[3]),
          'map_capacity' : int(cols[8]),
          'reduce_capacity' : int(cols[9])
        })

  def map(self):
    return self.cluster_summary['map_capacity']

  def reduce(self):
    return self.cluster_summary['reduce_capacity']

  def nodes(self):
    return self.cluster_summary['nodes']

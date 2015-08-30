class Demand:

  def __init__(self, doc):
    self.data = []
    running_jobs = doc.find("h2", {"id" : "running_jobs"}).findNextSibling("table", {"class" : "datatable"})
    table_body = running_jobs.find('tbody')
    if table_body != None:
      rows = table_body.findAll('tr')
      for row in rows:
          cols = row.findAll('td')
          cols = [ele.text.strip() for ele in cols]
          cols = [ele for ele in cols if ele] # Get rid of empty values
          if len(cols) > 1:
            # Columns are
            # - Jobid
            # - Priority
            # - User
            # - Name
            # - Map % Complete
            # - Map Total
            # - Maps Completed
            # - Reduce % Complete
            # - Reduce Total
            # - Reduces Completed
            # - Job Scheduling Information
            # - Diagnostic Info
            job = {
              "total_map": int(cols[5]),
              "total_reduce": int(cols[8])
            }
            self.data.append(job)


  def _pick_map(self, job):
    return job['total_map']

  def _pick_reduce(self, job):
    return job['total_reduce']

  def map(self):
    return sum(map(self._pick_map, self.data))

  def reduce(self):
    return sum(map(self._pick_reduce, self.data))

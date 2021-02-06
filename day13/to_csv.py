import csv

def save_to_csv(term, jobs):
  header = ["Title", "Company", "Link"]

  file = open(f"{term}.csv", mode='w')
  
  writer = csv.writer(file)
  writer.writerow(header)
  for job in jobs:
    writer.writerow(list(job.values()))
  
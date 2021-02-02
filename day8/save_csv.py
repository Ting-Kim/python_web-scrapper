import csv

def save_to_csv(brand, jobs):
  header = ["place", "title", "time", "pay", "date"]
  try:
    file = open(f"{brand}.csv", mode='w')
  except:
    brand = brand.replace("/", "", len(brand))
    file = open(f"{brand}.csv", mode='w')
  finally:
    writer = csv.writer(file)
    writer.writerow(header)
    for job in jobs:
      writer.writerow(list(job.values()))
  
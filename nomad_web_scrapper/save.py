
import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w") # w의 의미 : 쓰기
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "link"])
  for job in jobs:
    # writer.writerow(job.values())
    writer.writerow(list(job.values()))
  # print(jobs)
  return


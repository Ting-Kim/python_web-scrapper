from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
import os
from save import save_to_file

os.system("clear")

indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jobs = so_jobs + indeed_jobs
jobs = indeed_jobs

save_to_file(jobs)

# Comma Separated Values (CSV 파일)



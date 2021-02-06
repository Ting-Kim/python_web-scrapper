import requests
from flask import Flask, render_template, request, redirect, send_file
from ro import extract_ro
from so import extract_so
from wrr import extract_wrr
from to_csv import save_to_csv
import os
os.system("clear")

"""s
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask('ScrapperLast')
db = {'ro':{}, 'so':{}, 'wrr':{}}


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  term = request.args.get('term').lower()
  
  if term in db['ro']:
    ro = db['ro'][term]
  else:
    ro = extract_ro(term)
  
  if term in db['so']:
    so = db['so'][term]
  else:
    so = extract_so(term)
    
  if term in db['wrr']:
    wrr = db['wrr'][term]
  else:
    wrr = extract_wrr(term)

  job_list = ro+so+wrr
  save_to_csv(term, job_list)
  return render_template("search.html", term=term, jobs=job_list, count_jobs=len(job_list))

@app.route('/tocsv', methods=['GET','POST'])
def to_csv():
  args_dict = request.args.to_dict()
  term = args_dict['term']
  file_name = f"{term}.csv"
  return send_file(file_name, mimetype='text/csv', attachment_filename=f'{term}.csv', as_attachment=True)

app.run(host="0.0.0.0")
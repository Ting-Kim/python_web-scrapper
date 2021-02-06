import requests
from bs4 import BeautifulSoup as bs

URL = "https://weworkremotely.com"

def extract_wrr(term):
  url = f"{URL}/remote-jobs/search?term={term}"
  print(f'searching for {term} jobs at {url}... ')
  response = requests.get(url)
  bs_ = bs(response.text, 'html.parser')
  jobs_container = bs_.find('div', {'class':'jobs-container'})
  job_infos = jobs_container.find('ul').find_all('li')[:-1]

  wrr_list = []
  for job_info in job_infos:
    title = job_info.find('span', {'class':'title'})
    company = job_info.find('span', {'class':'company'}).text
    href = f"{URL}{title.parent['href']}"
    title = title.text
    wrr_list.append({"title":title, "company":company, "href":href})

  return wrr_list
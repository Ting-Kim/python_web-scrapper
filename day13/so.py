import requests
from bs4 import BeautifulSoup as bs

URL = "https://stackoverflow.com"

def extract_so(term):
  url = f"{URL}/jobs?r=true&q={term}"
  # print(f'searching for {term} jobs at {url}... ')
  last_page = int(get_last_page(url))

  so_list = []
  for page_num in range(1, last_page+1):
    response = requests.get(f"{url}&page={page_num}")
    print(f'searching for {term} jobs at {url}&page={page_num}... ')
    bs_ = bs(response.text, 'html.parser')
    # print(bs_)
    job_infos = bs_.find_all('div', {'class' : '-job'})
    for job_info in job_infos:
      job_info_h2 = job_info.find('h2')
      title = job_info_h2.text.strip()
      company = job_info.find('span').text.strip()
      href = job_info_h2.find('a')['href']
      href = f"{URL}{href}"
      so_list.append({'title':title, 'company':company, 'href':href})

  return so_list

def get_last_page(url):
  response = requests.get(url)
  bs_ = bs(response.text, "html.parser")
  pages = bs_.find("div", {"class":"s-pagination"}).find_all('a')
  last_page = pages[-2].get_text(strip=True)
  return last_page
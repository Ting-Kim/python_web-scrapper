import requests
from bs4 import BeautifulSoup as bs

URL = "https://remoteok.io"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_ro(term):
  url = ''.join([URL, "/remote-dev+{}-jobs".format(term)])
  print(f'searching for {term} jobs at {url}... ')
  response = requests.get(url, allow_redirects=False, headers=headers)
  
  bs_ = bs(response.text, 'html.parser')
  work_infos = bs_.find_all('td',{'class':'company_and_position_mobile'})

  ro_list = []

  for work_info in work_infos:
    title = work_info.find('h2')
    company = work_info.find('h3')
    if title is None or company is None:
      continue
    else:
      href = title.parent['href']
      href = ''.join([URL, href])
      title = title.text
      company = company.text

    ro_list.append({'title':title, 'company':company, 'href':href})

  return ro_list
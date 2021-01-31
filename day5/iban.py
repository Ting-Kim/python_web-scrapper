import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
URL = "https://www.iban.com/currency-codes"

def extract_iban():
  flag = True
  iban = requests.get(URL)
  soup = BeautifulSoup(iban.text, "html.parser")
  table = soup.find_all('table', {'class':'table table-bordered downloads tablesorter'})
    
  for element in table:
    tr = element.find_all('tr')
  
  tr_list = []
  for element in tr[1:]:
    tr_list.append(element.find_all('td'))
    
  country_info = []
  for element in tr_list:
    tmp = []
    for td in element:
      td_string = td.string

      # no currency_code
      if td_string is None:
        flag = False
        break
      tmp.append(td_string)
      
    if not flag:
      flag = True
      continue
  
    country_info.append(tmp)
  
  return country_info

def search_code(country_info):
  print('Hello! Please choose select a country by number:')
  for i in range(len(country_info)):
    print(f"# {i} {country_info[i][0]}")
  input_code(country_info)

def input_code(country_info):
  num = input("#: ")
  try:
    num = int(num)
    if num < 0 or num > len(country_info)-1:
      print("Choose a number from the list.")
      input_code(country_info)
      return
    else:
      print(f"You chose {country_info[num][0]}")
      print(f"The currency code is {country_info[num][2]}")
      return
  except:
    print("That wasn't a number.")
    input_code(country_info)
  
  return



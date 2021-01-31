import os
import requests
from bs4 import BeautifulSoup
import time

os.system("clear")
URL_CURRENCY_CODES = "https://www.iban.com/currency-codes"

def extract_iban():
  flag = True
  iban = requests.get(URL_CURRENCY_CODES)
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
  print('Welcom to CurrencyConvert PRO 2000\n')
  for i in range(len(country_info)):
    print(f"# {i} {country_info[i][0]}")
  print("where are you from? Choose a country by a number.\n")
  
  currency_from = input_func(country_info)
  currency_to = input_func(country_info)
  if currency_from == currency_to:
    print("Please input a another number.")
    return search_code(country_info)

  try:
    amount_to_convert = input_amount(currency_from, currency_to)
    result_amount = convert_currency(currency_from, currency_to, amount_to_convert)
    print(F"{currency_from}{amount_to_convert} is {currency_to}{result_amount}")


  except:
    print("\n** There is no conversion between them! **")
    print("\t\t#########################")
    print("\t\t#########################")
    print("\t\t### Program restart.. ###")
    print("\t\t#########################")
    print("\t\t#########################")
    print("\t\t#########################")
    time.sleep(2)
    search_code(country_info)
  
  return result_amount

def convert_currency(from_, to_, amount):
  url_conversion_currency = f"https://transferwise.com/gb/currency-converter/{from_}-to-{to_}-rate?amount={amount}"

  response_ = requests.get(url_conversion_currency)
  html = BeautifulSoup(response_.text, "html.parser")
  rate_conversion = float(html.find("input", {"id":"rate"})["value"])

  result_amount = amount * rate_conversion

  return result_amount


def input_func(country_info):
  try:
    num = int(input("#: "))
    if num < 0 or num > len(country_info)-1:
      print("Choose a number from the list.")
      return input_func(country_info)
    else:
      print(f"{country_info[num][0]}")
      return country_info[num][2]
  except:
    print("That wasn't a number.")
    return input_func(country_info)
  return country_info[num][2]


def input_amount(from_, to_):
  try:
    amount_for_convert = float(input("\nHow many {from_} do you want to convert to {to_}?\n"))
    
  except:
    print("That wasn't a number.")
    return input_amount(from_, to_)

  return amount_for_convert

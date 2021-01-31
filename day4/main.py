import requests
import os

def is_it_down():
  os.system('clear')
  print('Welcome to IsItDown.py!')
  
  urls = input('Please write a URL or URLs you want to check. (separated by comma)\n')
  http = 'http://'
  if ',' in urls:
    urls = urls.split(',')
  else:
    urls = [urls]
  
  if not is_valid_url(urls):
    continue_check()
    return
    
  for url in urls:
    url = url.strip()
    if http not in url:
        url = ''.join([http, url])
    try:
      r = requests.get(url)
      print(r.status_code)
      print(r.raise_for_status())
      if r.raise_for_status() is None:
        print(f"{url} is up!")
      else:
        print(f"{url} is down!")

    except:
      print(f"{url} is down!")
      continue_check()

  return continue_check()
    
  

def is_valid_url(urls_):
  for url_ in urls_:
    if '.' not in url_:
      print(f"{url_} is not a valid URL.")
      return False
    
  return True

def wanna_restart():
  answer = input('Do you want to start over? y/n\t')
  if answer == 'y' or answer == 'Y':
    return True
  elif answer == 'n' or answer == 'N':
    return False
  else:
    print("That's not a valid answer.")
    return wanna_restart()

def continue_check():
  if not wanna_restart():
      print('k. bye!')
      return
  else:
    is_it_down()

## func on
is_it_down()
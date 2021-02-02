import os
from scrapper import extract_brand, extract_recruit
from save_csv import save_to_csv

os.system("clear")
alba_url = "http://www.alba.co.kr"

brand_list = extract_brand(alba_url)

for brand in brand_list:
  job = extract_recruit(brand["brand_link"])
  brand = brand["brand_name"]
  save_to_csv(brand, job)

## For test
# job = extract_recruit(brand_list[0]["brand_link"])
# brand = brand_list[0]["brand_name"]
# save_to_csv(brand, job)
# 이전 강의 코드 #2.3~#2.5
# from indeed import extract_indeed_pages, extract_indeed_jobs
# last_indeed_page = extract_indeed_pages()
# extract_indeed_jobs(last_indeed_page)

from iban import extract_iban, search_code

country_info = extract_iban()
search_code(country_info)


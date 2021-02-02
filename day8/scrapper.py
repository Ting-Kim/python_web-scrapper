import requests
from bs4 import BeautifulSoup as bs

def extract_brand(url):
  response = requests.get(url)
  bs_ = bs(response.text, "html.parser")
  super_brands = bs_.find("div", {"id":"MainSuperBrand"}).find_all("a",{"class":"goodsBox-info"})
  link_super_brands = []
  for super_brand in super_brands:
    link_super_brands.append({"brand_name":super_brand.find("span", {"class":"company"}).string,
                              "brand_link": super_brand["href"]})
  
  return link_super_brands

def extract_recruit(url):
  page_num = 1
  recruit_info = [] # place,title,time,pay,date 정보를 담을 리스트
  while True:
    print("\n########################################################################################################")
    print(f"\t\t현재 추출 중인 URL : {url}job/brand/?page={page_num}")
    print("########################################################################################################\n")
    response = requests.get(f"{url}job/brand/?page={page_num}")
    try: 
      response = requests.get(f"{url}job/brand/?page={page_num}")
      bs_ = bs(response.text, "html.parser")
      box_logo_list = bs_.find("div", {"class":"goodsList"})
      recruit_list = box_logo_list.find_all("tr")

      for i in range(len(recruit_list)):
        if i % 2 != 0:
          info = recruit_list[i]
          
          place = info.find("td", {"class":"local first"}).find(text=True)
          store_name = info.find("td", {"class":"title"}).find("span", {"class":"company"}).string
          work_time = info.find("td", {"class":"data"}).find("span").string
          pay = ''.join([info.find("td", {"class":"pay"}).find("span",{"class":"payIcon"}).string,
                        info.find("td", {"class":"pay"}).find("span",{"class":"number"}).string])
          reg_date = info.find("td", {"class":"regDate last"}).string
          
          recruit_info.append({
              "place":place,
              "title":store_name,
              "time":work_time,
              "pay":pay,
              "date":reg_date
          })

    except:
      print("채용정보가 존재하지 않거나, 페이지가 끝에 도달하였습니다.")
      recruit_info.append({
        # "place":info.find("td").string,
        "place":"데이터가 존재하지 않거나 더이상 불러올 데이터가 없습니다",
        "title":"-",
        "time":"-",
        "pay":"-",
        "date":"-"
      })
      return recruit_info
    
    page_num += 1
      

  return recruit_info

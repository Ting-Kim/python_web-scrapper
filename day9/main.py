import requests
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import json

import os
os.system("clear")

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"
app = Flask("DayNine")
db = {}

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

# Search items by id
items = f"{base_url}/items"

@app.route("/")
def ting_news_home():
  try:
    order_by = request.args.get('order_by')
    if order_by: # None이 아닌 경우
      order_by = order_by.lower()
    if order_by == 'new':
      if order_by in db:
        response = db[order_by]
      else:
        response = requests.get(new)
        db[order_by] = response
    else:
      order_by = 'popular'
      if order_by in db:
        response = db[order_by]
      else:
        response = requests.get(popular)
        db[order_by] = response
    news_list = response.json()['hits'] # API Result
  except:
    return redirect("/")
  print(db)
  return render_template("index.html", news_list=news_list, order_by=order_by)


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
@app.route("/<id>")
def make_detail_url(id):
  try:
    if id in db:
      response = db[id]
    else:
      response = requests.get(f"{items}/{id}")
      db[id] = response
    items_list = response.json()
    if "error" in items_list:
      return redirect("/")
  
  except:
    return redirect("/")
  print(db)
  return render_template("detail.html", news=items_list)

app.run(host="0.0.0.0")
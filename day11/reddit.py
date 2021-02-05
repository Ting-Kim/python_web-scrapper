import requests
from bs4 import BeautifulSoup as bs

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

URL = "https://reddit.com"

def extract_post(subreddit):
  url = ''.join([URL, "/r/{}".format(subreddit), "/top/?t=month"])
  response = requests.get(url, headers=headers)
  soup = bs(response.text, 'html.parser')
  posts = soup.find_all('div', {'class':'_1oQyIsiPHYt6nx7VOmd1sz'})
  post_info = []
  for post in posts:
    vote_post = post.find('div', {'class':'_1rZYMD_4xY3gRcSS3p8ODO'})
    vote_span = vote_post.find('span', {'class':'D6SuXeSnAAagG8dKAb4O4'})
    vote = vote_span.string if vote_span else vote_post.string
    # vote >= 1000 일 때 1.0k 형태로 표현 /  'vote'는 0으로 취급
    if vote[-1] == 'e':
      vote = 0
    elif vote[-1] == 'k':
      vote = int(float(vote.rstrip('k')) * 1000)
    else:
      vote = int(vote)

    title = post.find('h3', {'class':'_eYtD2XCVieq6emjKBH3m'}).string

    href = post.find('a', {'class':'SQnoC3ObvgnGjWt90zD9Z'})

    if href:
      href = ''.join([URL, href['href']])
    else: 
      continue

    post_info.append({'title' : title, 'upvotes': vote, 'subreddit':subreddit, 'href':href})
    
  return post_info
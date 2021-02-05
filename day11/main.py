import requests
from flask import Flask, render_template, request, redirect
from reddit import extract_post

import os
os.system("clear")

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")
db = {}

extract_post(subreddits[-1])

@app.route("/")
def reddit_reader_home():
  return render_template('home.html', subreddits=subreddits)


@app.route('/read')
def reddit_read_for_sub():
  try:
    on_subreddits = request.args # 리스트
    for i, on_subreddit in enumerate(on_subreddits):
      if on_subreddit in db:
        infos = db['on_subreddit']
      else: 
        infos = extract_post(on_subreddit)
        db['on_subreddit'] = infos

      if i == 0:
        post_infos = infos
      else:
        post_infos = post_infos + infos

    post_infos.sort(key=lambda x: x['upvotes'], reverse=True)

  except:
    print("Something Error, go back to homepage.")
    return redirect("/")
  return render_template('read.html', subreddits=on_subreddits, post_infos=post_infos)


app.run(host="0.0.0.0")
import requests
import json
from database import *
from datetime import datetime

headers = {
    "Accept": "application/json",
    "Api-Key": "f324078d3655222f780cab5e4c38f5e771c6795c87072aff0db3fe0a38c4e0fa",
    "Api-Username": "",
}
params = {
    "headers": headers
}


def create_topic(post_id, body, title, username):
    data = {
        "raw": body,
        "title": title
    }
    headers["Api-Username"] = username
    res = requests.post("https://mypwcforum.com/posts.json", data=data, headers=headers )
    if res.status_code == 200:
        jres = res.json()
        store_post(post_id=post_id, topic_id=jres["topic_id"])
        print("successfully created topic.")
    else:
        print("error creating discord topic. Did not store.")
    return res.json()

def build_url(discourse_post):
    link_to_index = ""
    try:
        link_to_index = "https://mypwcforum.com/t/" + discourse_post["topic_slug"] + "/" + str(discourse_post["topic_id"])
        return link_to_index
    except:
       return link_to_index

def create_post_reply(comment_id, body, topic_id, comment_headers):
    data = {
        "raw": body,
        "topic_id": topic_id
    }
    res = requests.post("https://mypwcforum.com/posts.json", data=data, headers=comment_headers)
    if res.status_code == 200:
        store_comment(comment_id=comment_id)
    else:
        print('error creating comment. Did not store.')

    return res
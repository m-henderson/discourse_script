import requests
import random
from utils.dicourse import *
from database import *
import time

headers = {
    "Accept": "application/json; charset=utf-8",
    "Api-Key": "",
    "Api-Username": "",
}
params = {
    "headers": headers
}

def should_process_comment(comment_body):
    return (len(comment_body) >= 20)

def process_comments(user_names, post, posted_by):
    if (post["comments_full"] is None) == False:
        for comment in post['comments_full']:
            if len(comment["comment_text"]) > 20:
                if comment_exist(comment["comment_id"]):
                    print('comment exist...skipping. ' + comment["comment_id"])
                else:
                    headers["Api-Username"] = random.choice(user_names)
                    # commenter should not comment on their own post.
                    if (headers["Api-Username"] == posted_by):
                        headers["Api-Username"] = random.choice(user_names)
                    topic_id = get_discourse_post_id(post["post_id"])
                    if topic_id:
                        create_post_reply(comment_id=comment["comment_id"], body=comment["comment_text"], topic_id=topic_id, comment_headers=headers)
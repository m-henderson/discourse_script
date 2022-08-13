# imports
from dotenv import load_dotenv
from facebook_scraper import get_posts
from users import *
from comments import *
from post import *
from utils.dicourse import *
from utils.tools import *
import os
import random
from database import *

# init tables
create_tables()

# load env variables
load_dotenv()

# fb scrape options
options = {"comments": "generator"}

# fields
user_names = []
group = os.environ["fb_group"]
pages = os.environ["pages"]
cookies = os.environ["cookies"]

# type conversions for env var
pages = int(pages)

# load users
user_names = get_usernames()

# being process
for post in get_posts(group=group, pages=pages, cookies=cookies, options=options):
    if (should_process(post["text"])):
        if post_exist(post["post_id"]):
            user_name = random.choice(user_names)
            process_comments(user_names=user_names, posted_by=user_name, post=post)
        else:
            cleaned_body = clean_text_body(post["text"])
            cleaned_title = generate_title(cleaned_body)
            image_links = get_image_links(post)
            
            for image_link in image_links:
                cleaned_body = cleaned_body + "\n" + image_link + "\n"
            video_link = get_video_link(post)
            if video_link:
                cleaned_body = cleaned_body + "\n" + video_link

            user_name = random.choice(user_names)
            discourse_topic = create_topic(post_id=post["post_id"], body=cleaned_body, title=cleaned_title, username=user_name)
            link = build_url(discourse_post=discourse_topic)
            #google_index_url(link)
            bing_index_url(link)
            process_comments(user_names=user_names, posted_by=user_name, post=post)


        

        
    
        




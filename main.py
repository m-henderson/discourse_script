# imports
from dotenv import load_dotenv
from facebook_scraper import get_posts
from users import *
from post import *
import os

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
    print(post['text'][:50])


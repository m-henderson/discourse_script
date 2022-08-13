from writefull import generate_title
from utils.tools import clean_text_body

# decides if we should even process the post
# - post must be of proper length in the body (at least 100 characters)
def should_process(post):
    return (len(post) >= 150) and (len(post) <= 2000)

# begin post processing. post processing is when
# we begin building the title, spacing the body, 
# 
def process_post(post):
    # clean body
    clean_body = clean_text_body(post["text"])
    #process_comment(post["comments_full"])
    title = generate_title(clean_body)
    return title




def get_post_title(title):
    generate_title(title)
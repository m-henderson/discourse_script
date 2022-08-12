from utils.importing import import_json

posts = import_json('tests/models/posts.json')

def short_body_post():
    return posts[1]["short_body"]

def long_body_post():
    return posts[0]["long_body"]
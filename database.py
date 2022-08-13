import sqlite3 as sl

# database.py >
import sqlite3 as sl

# database connection
con = sl.connect('data.db')
cur = con.cursor()

def create_tables():
    cur.execute('''CREATE TABLE IF NOT EXISTS posts (post_id text, discourse_post_id integer)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS comments (comment_id text)''')
    con.commit()

def table_exist(name):
    cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?",(name,))
    if cur.fetchone()[0]==1:
        return True
    else:
        return False

def post_exist(post_id):
    row = cur.execute("SELECT post_id from posts where post_id = ?",(post_id,),).fetchone()
    if row != None:
        return True
    else:
        return False

def comment_exist(comment_id):
    row = cur.execute("SELECT comment_id from comments where comment_id = ?",(comment_id,),).fetchone()
    if row != None:
        return True
    else:
        return False

def store_comment(comment_id):
    cur.execute("INSERT INTO comments VALUES (?)", (comment_id,))
    con.commit()

def store_post(post_id, topic_id):
    cur.execute("INSERT INTO posts VALUES (?, ?)", (post_id, topic_id,))
    con.commit()

def indexed_by_bing(discourse_post_id):
    row = cur.execute("SELECT discourse_post_id from bing where discourse_post_id = ?",(discourse_post_id,),).fetchone()
    if row != None:
        return True
    else: 
        return False
    
def get_discourse_post_id(post_id):
    row = cur.execute("SELECT discourse_post_id from posts where post_id = ?",(post_id,),).fetchone()
    return row




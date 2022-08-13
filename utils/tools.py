import re
import requests
import json
def clean_text_body(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    removed_emojis = re.sub(emoj, '', data)
    return removed_emojis.replace("\n", "")

def get_image_links(post):
    if (len(post["images"]) > 0):
        return post["images"]
    else:
        return []

def get_video_link(post):
    if post["video"] is not None:
        return post["video"]

def google_index_url(link):
    print("")

bing_url = "https://ssl.bing.com/webmaster/api.svc/json/SubmitUrl?apikey=f124cf278d2a414487f95a13a6f101a0"
headers = {
    "Content-Type": "application/json; charset=utf-8"
}
siteUrl = "https://mypwcforum.com"
data = {
    "siteUrl": siteUrl, 
    "url": ""
}

def bing_index_url(index_url):
    data["url"] = index_url
    jdata = json.dumps(data)
    req = requests.request("POST", headers=headers, url=bing_url, data=jdata)
    if req.status_code == 200:
        print("succesfully indexed URL with Bing. " + str(index_url))
    return req

def append_videos(video_links):
    print("")


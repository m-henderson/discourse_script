from requests import post
import json
# what if we get an error on writefull api? how do we check status codes
def generate_title(title):
    arr = []
    arr.append(title)
    data = json.dumps(arr)
    # needs to be in array ["atest"]
    test = post("https://x-api.writefull.com/title-generator", data=data, headers={"Content-Type":"application/json", "Accept": "*/*"})
    if test.status_code == 200:
        return test.text.strip("[]").strip('"')
    else:
        return title[:50]
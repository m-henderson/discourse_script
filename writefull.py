
import openai
openai.api_key = "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"

import json
# what if we get an error on writefull api? how do we check status codes
def generate_title(discourse_post_body):
    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo" ,
    max_tokens = 280,
    messages = [
            {"role": "system", "content": "Generate a title no longer than 40 characters to the text I am about to give you."},
            {"role": "user","content": discourse_post_body}
    ])
    
    message = response.choices[0]['message']
    return message




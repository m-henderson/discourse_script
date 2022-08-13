from utils.importing import import_json

posts = import_json('tests/models/posts.json')

def short_body_post():
    return posts[1]["short_body"]

def long_body_post():
    return posts[0]["long_body"]

# a dirty post that contains emojis and ASCII
def dirty_body_post():
    return '⚠️ AVOIDING SCAMMERS ⚠️\n\nHey friends 👋🏻\nI hope everyone is enjoying their holidays.\nI’m still slowly weeding out the scammers in this group of 18k members. Besides spotting the obvious scammers that can’t answer the member questions correctly, there are others who know the game, and play it well. These scammers are smart. They steal information on a legit profile, post pics of families, update statuses, etc. so they look real.\nAlthough the group has cleaned up quite a bit, this does not mean that you should still trust everyone in this group, ESPECIALLY when it comes to sales.\n-DO NOT assume people are who they say they are. Not sure if someone is legit? Search their name in the jetski groups to see if anybody has had any bad dealings with them.\n-DO NOT pay via friends and family. We get it, you’re broke AF, we all are. Just pay the extra fees for goods and services and lessen your risk of not getting your money back. I have very little sympathy for members who don’t pay the fees and then come crying when they get screwed over.\n-Had a bad transaction with a member? Call them out so others are aware, but be ready to show proof if the member decides to defend themselves.\n\nThat’s all I’ve got for now 😂 feel free to comment any other selling tips below ⬇️\nI wish everyone a very Happy Holiday and Happy New Year 🎄\n\nVideo of a bunch of whales for your time 🤘🏻🐋'

def clean_body_post():
    return ' AVOIDING SCAMMERS Hey friends I hope everyone is enjoying their holidays.I’m still slowly weeding out the scammers in this group of 18k members. Besides spotting the obvious scammers that can’t answer the member questions correctly, there are others who know the game, and play it well. These scammers are smart. They steal information on a legit profile, post pics of families, update statuses, etc. so they look real.Although the group has cleaned up quite a bit, this does not mean that you should still trust everyone in this group, ESPECIALLY when it comes to sales.-DO NOT assume people are who they say they are. Not sure if someone is legit? Search their name in the jetski groups to see if anybody has had any bad dealings with them.-DO NOT pay via friends and family. We get it, you’re broke AF, we all are. Just pay the extra fees for goods and services and lessen your risk of not getting your money back. I have very little sympathy for members who don’t pay the fees and then come crying when they get screwed over.-Had a bad transaction with a member? Call them out so others are aware, but be ready to show proof if the member decides to defend themselves.That’s all I’ve got for now  feel free to comment any other selling tips below I wish everyone a very Happy Holiday and Happy New Year Video of a bunch of whales for your time '

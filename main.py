import praw
import time
reddit = praw.Reddit(client_id='09tgNAaa_kchTA',
                     client_secret='EqtcxF2IqjbUwT5uh3sSGXmQ8b0wfg',
                     user_agent='a reddit instance',
                     username='Alert-Target-8166',
                     password='poggers', )
def subspam():
    misctext = "a"  # miscellaneous message
    # customised messages for each subreddit
    textamong = "a"
    textgaming = "a"
    textmobile = "a"
    textshopping = "a"

    subname = 'AmongUs+gaming+MobileGaming+Shopping' # obviously you can add more subreddits to this
    usedusernames = []
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author.name
        title = f'Hello, {name}'
        if name in usedusernames:
            continue
        try:
            if comment.subreddit.display_name == "AmongUs":
                text = textamong
            elif comment.subreddit.display_name == "gaming":
                text = textgaming
            elif comment.subreddit.display_name == "MobileGaming":
                text = textmobile
            elif comment.subreddit.display_name == "Shopping":     # if you can add more of these personalised ones
                text = textshopping
            else:
                text = misctext
            reddit.redditor(name).message(title, text)
        except:
            continue
        usedusernames.append(name)
        print(f'u/{name} r/{comment.subreddit.display_name}')
        time.sleep(40)


subspam()

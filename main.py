import praw
import time

reddit = praw.Reddit(client_id='01tuOpG6GAHSIQ',
                     client_secret='0nQyf-5h7UY4RfzZD0FytbICzpN-Iw',
                     user_agent='a reddit instance',
                     username='ImpostermeOffical',
                     password='Project2020')


def subspam():
    misctext = "Don’t miss out on the limited edition release of the Crewmate Plushy, limited quantities remaining! Get yours today at Imposterme.com"  # miscellaneous message

    subname = 'AmongUs+gaming+MobileGaming+Shopping'  # obviously you can add more subreddits to this
    usedusernames = []
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author.name
        title = f'Hello, {name}'
        if name in usedusernames:
            continue
        try:
            text = misctext
            reddit.redditor(name).message(title, text)
        except:
            continue
        usedusernames.append(name)
        print(f'u/{name} r/{comment.subreddit.display_name}')
        time.sleep(40)
subspam()


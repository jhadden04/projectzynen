import praw
import time
import random
reddit = praw.Reddit(client_id='01tuOpG6GAHSIQ',
                     client_secret='0nQyf-5h7UY4RfzZD0FytbICzpN-Iw',
                     user_agent='a reddit instance',
                     username='ImpostermeOffical',
                     password='Project2020')
def imageposter():
    while True:
        subname = 'AmongUs+gaming+MobileGaming+Shopping'
        subreddits = ["AmongUs", "gaming", "MobileGaming", "Shopping"]
        x = random.randint(0, (len(subreddits)-1))
        subreddit = reddit.subreddit(subreddits[x])
        titles = ["change this"]  # you must change this to your desired title
        reddit.validate_on_submit = True
        images = ["C:\\Users\\jhadd\\Pictures\\discord bot.PNG"]  # you must change this to the path on your computer, and use double slashes
        try: 
            subreddit.submit_image(titles[0], images[0])
        except: 
            continue
        print(f'Image posted')
        time.sleep(3600)


imageposter()

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
        titles = ["Don’t miss out on the limited edition release of the Crewmate Plushy, limited quantities remaining! Get yours today at Imposterme.com"]  # you must change this to your desired title
        reddit.validate_on_submit = True
        images = ["C:\\Users\\thein\\Pictures\\snapchatad.jpg"]  # you must change this to the path on your computer, and use double slashes
        subreddit.submit_image(titles[0], images[0])
        print(f'Image posted')
        time.sleep(3600)


imageposter()

import praw
import time

reddit = praw.Reddit(client_id='01tuOpG6GAHSIQ',
                     client_secret='0nQyf-5h7UY4RfzZD0FytbICzpN-Iw',
                     user_agent='a reddit instance',
                     username='ImpostermeOffical',
                     password='Project2020')
def imageposter():
    while True:
        subreddit = reddit.subreddit('AmongUs+gaming+MobileGaming+Shopping')
        titles = ["change this"] # you must change this to your desired title
        reddit.validate_on_submit = True
        images = ["C:\\Users\\jhadd\\Pictures\\discord bot.PNG"]  # you must change this to the path on your computer, and use double slashes
        subreddit.submit_image(titles[0], images[0])
        print(f'Image posted')
        time.sleep(3600)

imageposter()

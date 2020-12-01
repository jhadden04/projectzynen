import praw
import time

reddit = praw.Reddit(client_id='01tuOpG6GAHSIQ',
                     client_secret='0nQyf-5h7UY4RfzZD0FytbICzpN-Iw',
                     user_agent='a reddit instance',
                     username='ImpostermeOffical',
                     password='Project2020')

def keyword():
    trigger_phrase = ["Among Us toy", "among us toy"]  # you can expand this/change this
    while True:
        for comment in reddit.subreddit('AmongUs+gaming+MobileGaming+Shopping+Johntesting').stream.comments():
            # check the trigger_phrase in each comment
            n = 0
            for i in range(len(trigger_phrase)):
                n += 1
                if trigger_phrase[n-1] in comment.body:
                    # extract the word from the comment
                    name = comment.author.name
                    title = f'Hello, {name}'
                    text = 'Don’t miss out on the limited edition release of the Crewmate Plushy, limited quantities remaining! Get yours today at Imposterme.com'
                    try:
                        reddit.redditor(name).message(title, text)
                    except:
                        continue
                    print(f'u/{name}, Comment body: {comment.body}')
                    time.sleep(5)
                    continue
keyword()

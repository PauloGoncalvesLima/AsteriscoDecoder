import re
import praw
import colorit
import time


subreddits = ['desabafos', 'brasil', 'Dota2Brasil']
total = 0
reddit = praw.Reddit('BotCrawler')

palavrasConhecidas = dict()

with open("") as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val

def wait(time2wait):
    if(time2wait >= 60):
        total = 0
        time.sleep(time2wait) 


# for subs in subreddits:
for submission in reddit.subreddit('desabafos').hot(limit= 1):
    total += 1
    wait(total)
    text = fixString(submission.selftext)
    print(colorit.color_front (text, 255,255,0))

    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]  # Seed with top-level
    while comment_queue:
        comment = comment_queue.pop(0)
        text = fixString(comment.body)
        print(text)
        comment_queue.extend(comment.replies)
        total += 1
        wait(total)





    # for comment in submission.comments:
    #     print(colorit.color_front (comment.body, 0, 255, 0))
    #     total += 1
    #     wait(total)
    #     comment.reply_sort = "new"
    #     comment.refresh()

    #     for replie in comment.replies:
    #         print(colorit.color_front (replie.body, 255, 0, 255))
    #         total += 1
    #         wait(total)

    #         for replieInreplie in replie.replies:
    #             print(colorit.color_front (replieInreplie.body, 255, 165, 0))
    #             total += 1
    #             wait(total)
            
       


# wordsSet = open('./palavras.txt')
# addSet = open('./processedWords.txt')

# wordsSet.read().split('\n')
# addSet.read().split()

# [palavra for palavra in palavras if palavra not in stopwords]

# for i in range(0, len(words)-1):
#     words[i] += '\n'
#     file.write(words[i] )
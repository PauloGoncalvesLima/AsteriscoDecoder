import re
import praw
import colorit
import time
import textCleaner
#3629
LIMIT = 5000
subreddits = ['desabafos', 'brasil', 'Dota2Brasil']
total = 0
reddit = praw.Reddit('BotCrawler')

palavrasConhecidas = set()
sentenceFile = open("./texts/redditSentences.txt",'a')

with open("./texts/cleanWords.txt", encoding="utf8") as f:
    for line in f:
       palavrasConhecidas.add(line)
f.close()

def wait(time2wait):
    if(time2wait >= 60):
        print("esperando 60s")
        time.sleep(time2wait)
        time2wait = 0
    return time2wait

def placeInSet(text):
    for word in text.split():
        palavrasConhecidas.add(word)

progress = 0
# for subs in subreddits:
for submission in reddit.subreddit('desabafos').hot(limit= LIMIT):
    progress += 1
    print(str(progress) + "/" + str(LIMIT))
    total += 1
    total = wait(total)
    for sentence in textCleaner.clear(submission.selftext):
        placeInSet(sentence)
        sentenceFile.write(sentence + '\n')

    # print(colorit.color_front (text, 255,255,0))

    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]  # Seed with top-level
    while comment_queue:
        comment = comment_queue.pop(0)
        for sentence in textCleaner.clear(comment.body):
            placeInSet(sentence)
            sentenceFile.write(sentence + '\n')
        # print(text)
        comment_queue.extend(comment.replies)
        # total += 1
        # wait(total)

sentenceFile.close()

wordFile = open("./texts/cleanWords.txt", 'w')
for w in palavrasConhecidas:
    wordFile.write(w)
wordFile.close()



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
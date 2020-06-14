import unicodedata

finalWords = open("./texts/cleanWords.txt", "a")
finalSentences = open("./texts/sentencesStartEnd.txt", "w")


# with open("./palavras.txt", encoding="utf8")as f:
#     for line in f:
#         line = str(unicodedata.normalize('NFD', line)\
#                 .encode('ascii', 'ignore')\
#                 .decode("utf8"))
#         line = line.lower()
#         finalWords.write(line)

with open("./texts/redditSentences.txt", encoding="utf8")as f:
    for line in f:
        line = "<COM> " + line[:len(line)-1] + " <FIM>\n"
        finalSentences.write(line)
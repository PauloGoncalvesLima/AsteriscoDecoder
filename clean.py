import unicodedata

finalWords = open("./cleanWords.txt", "a")


with open("./palavras.txt", encoding="utf8")as f:
    for line in f:
        line = str(unicodedata.normalize('NFD', line)\
                .encode('ascii', 'ignore')\
                .decode("utf8"))
        line = line.lower()
        finalWords.write(line)

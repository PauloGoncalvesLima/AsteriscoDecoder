import re
import unicodedata

def clear(completeText):

    parenteses = "\[|\]|\{|\}|\(|\)|\'|\"|<|>|~|^|´|`|°|$|%|º|ª|\*"
    numeros = "[0-9]+"
    # urlRe = "((?<=[^a-zA-Z0-9])(?:https?\:\/\/|[a-zA-Z0-9]{1,}\.{1}|\b)(?:\w{1,}\.{1}){1,5}(?:com|org|edu|gov|uk|net|ca|de|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil|iq|io|ac|ly|sm){1}(?:\/[a-zA-Z0-9]{1,})*)"
    urlRe = "\.com|https?|@|\.br|\/\/|\.[A-z0-9]+\."
    textList = []

    completeText = completeText.lower()
    completeText = str(unicodedata.normalize('NFD', completeText)\
           .encode('ascii', 'ignore')\
           .decode("utf-8"))
    completeText = re.sub(parenteses, ' ', completeText)
    completeText = re.sub(numeros, '<NUM>', completeText)
    completeText = completeText.split(' ')
    
    for word in completeText:  
        if not re.search(urlRe, word):
            textList.append(word)
    
    completeText = " ".join(textList)

    subPontuacao = r'([\.\!\?])[\.\!\?\s]*'
    completeText = re.sub(subPontuacao, r'\1', completeText)

    completeText = re.sub("([\.\,\!\?\;\:])", r' \1 ', completeText)

    completeText = ' '.join(completeText.split())# Tirar todos os espaços a mais
    pontuacao = r"([\.\!\?])"

    completeText = [a for a in re.split(pontuacao, completeText) if a != ""]
    finalText = []
   
    if len(completeText) % 2 != 0:
        completeText.append('.')

    for i in range(0, len(completeText), 2):
        finalText.append(completeText[i] + ' ' + completeText[i+1])

    return finalText 
    

testTex = input()


print(clear(testTex))


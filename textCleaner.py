import re
import unicodedata

# ERROS
# smiley :)
# etc. (palavras com ponto)
# subreddit (r/.....)

def clear(completeText):

    parenteses = r"\[|\]|\{|\}|\(|\)"
    charEspeciais = r"\'|\"|<|>|~|^|´|`|°|$|%|º|ª|\*|\_"
    numeros = r"[0-9]+"
    urlRe = r"\.com|https?|@|\.br|\/\/|\.[A-z0-9]+\."
    textList = []

    completeText = completeText.lower()
    completeText = str(unicodedata.normalize('NFD', completeText)\
           .encode('ascii', 'ignore')\
           .decode("utf-8"))
    completeText = re.sub(parenteses, ' ', completeText)
    completeText = completeText.split(' ')
    
    for word in completeText:  
        if not re.search(urlRe, word):
            textList.append(word)
    
    completeText = " ".join(textList)

    completeText = re.sub(charEspeciais, '', completeText)
    completeText = re.sub(numeros, '<NUM>', completeText)

    subPontuacao = r'([\.\!\?])[\.\!\?\s]*'
    completeText = re.sub(subPontuacao, r'\1', completeText)

    completeText = re.sub(r"([\.\,\!\?\;\:])", r'\1', completeText)

    completeText = ' '.join(completeText.split()) # Tirar todos os espaços a mais
    pontuacao = r"([\.\!\?])"

    completeText = [a for a in re.split(pontuacao, completeText) if a != ""]
    finalText = []
   
    if len(completeText) % 2 != 0:
        completeText.append('.')

    for i in range(0, len(completeText), 2):
        finalText.append(completeText[i] + ' ' + completeText[i+1])

    return finalText
from bs4 import BeautifulSoup
import requests

def writeJpWord(filename, item):
    text = item.find('a', class_="cue").text
    filename.write(text + "\n")

def writePrc(filename, item):
    prc = item.find('span', class_="transliteration")
    if prc is not None:
        filename.write(prc.text + "\n")
    else:
        filename.write("\n")

def writeMeaning(filename, item):
    meaning = item.find('p', class_="response").text
    filename.write(meaning + "\n")

def writeJpSentence(filename, item):
    itemSentence = item.find('div', class_="item-sentences")
    jpSent = itemSentence.find('p', class_="text").text
    filename.write(jpSent + "\n")

def writeEnSentence(filename, item):
    itemSentence = item.find('div', class_="item-sentences")
    enSent = itemSentence.find('p', class_="translation").text
    filename.write(enSent + "\n")


def getJpWord(item):
    text = item.find('a', class_="cue").text
    return text

def getPrc(item):
    prc = item.find('span', class_="transliteration")
    if prc is not None:
        return prc.text
    return " "

def getMeaning(item):
    meaning = item.find('p', class_="response").text
    return meaning

def getJpSentence(item):
    itemSentence = item.find('div', class_="item-sentences")
    jpSent = itemSentence.find('p', class_="text").text
    return jpSent

def getEnSentence(item):
    itemSentence = item.find('div', class_="item-sentences")
    enSent = itemSentence.find('p', class_="translation").text
    return enSent
    
    
    

#By right, we make a GET request(http://www.....).text to get the source code of
#web page.

#.. But because this japanese website dynamically fills the DOM, we cant
#access all the values.
with open('test.html', encoding='utf8') as htmlFile:
    soup = BeautifulSoup(htmlFile, 'html.parser')

    
testF = open("text.txt", 'w', encoding='utf8')
prcF = open("prc.txt", 'w', encoding='utf8')
meanF = open("meaning.txt", 'w', encoding='utf8')
jpSentF = open("jpSent.txt", 'w', encoding='utf8')
enSentF = open("enSent.txt", 'w', encoding='utf8')
dataF = open("dataF.txt", 'w', encoding='utf8')
for item in soup.find_all('li', class_="item"):
    writeJpWord(testF, item)
    writePrc(prcF, item)
    writeMeaning(meanF, item)
    writeJpSentence(jpSentF, item)
    writeEnSentence(enSentF, item)

    jpWord = getJpWord(item)
    prc = getPrc(item)
    meaning = getMeaning(item)
    jpSent = getJpSentence(item)
    enSent = getEnSentence(item)
    myStr = jpWord + "/" + prc + "/" + meaning + '/' + jpSent + '/' + enSent + "\n"
    dataF.write(myStr)

testF.close()
prcF.close()
meanF.close()
jpSentF.close()
enSentF.close()
dataF.close()

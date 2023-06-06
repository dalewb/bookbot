with open("books/frankenstein.txt") as f:
    text = f.read()

alphabetStr = "abcdefghijklmnopqrstuvwxyz"

def countAllLetters(text) -> int:
    letterCount = {}
    for el in text:
        letter = el.lower()
        if letter in alphabetStr:
            if not letterCount.get(letter):
                letterCount[letter] = 1
            else:
                letterCount[letter] += 1
    return letterCount

def mostCommonWord(wordList: list) -> tuple:
    allWords = {}
    mostCommonWord = ""
    occurences = 0
    for word in wordList:
        if not allWords.get(word):
            allWords[word] = 0
        allWords[word] =   allWords[word] + 1
        if allWords[word] > occurences:
            mostCommonWord = word
            occurences = allWords[word]
    return (mostCommonWord, occurences)

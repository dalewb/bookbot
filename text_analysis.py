import collections
import operator

class TextAnalysis:
    def __init__(self, title, text):
        self.title = title
        self.text = text 
        self.alphabetStr = "abcdefghijklmnopqrstuvwxyz"
        self.letterCount = None
        self.mostCommonWord = None

    def countAllLetters(self, text: str = None) -> int:
        if text is None:
            text = self.text
        if not self.letterCount:
            letterCount = {}
            for el in text:
                letter = el.lower()
                if letter in self.alphabetStr:
                    if not letterCount.get(letter):
                        letterCount[letter] = 1
                    else:
                        letterCount[letter] += 1
            self.letterCount = letterCount
        return self.letterCount

    def getMostCommonWord(self, wordList: list = None) -> tuple:
        if wordList is None:
            wordList = self.text.split(" ")
        if not self.mostCommonWord:
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
            self.mostCommonWord = (mostCommonWord, occurences)
        return self.mostCommonWord

    def sortDict(self, dictToSort: dict) -> dict:
        sortedDict = dict(sorted(dictToSort.items(), key=lambda item: item[1]))
        return sortedDict

    def generateReport(self):
        mostCommonWord = self.getMostCommonWord()
        letterCount = self.countAllLetters()
        allLetters = self.sortDict(self.letterCount)

        print(f"Report for {self.title}")
        print("---begin---")
        for letter, count in allLetters.items():
            print(f"The '{letter} character was found {count} times.'")
        
        print("---end---")

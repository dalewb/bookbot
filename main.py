from text_analysis import TextAnalysis

with open("books/frankenstein.txt") as f:
    text = f.read()

franken = TextAnalysis("Frankenstein", text)
franken.generateReport()
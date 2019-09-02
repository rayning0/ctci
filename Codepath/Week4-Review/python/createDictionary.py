# Problem: Design a method to find the number of occurrences of any given word in a book. 
# A word is represented as a String and a book is represented as a list of strings.
# This method will be called multiple times.
def createDictionary(book):
    if not book:
       return None
    dictionary = {}
    for word in book:
        word = word.strip()
        if word:
            word = word.lower()
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] = dictionary[word] + 1
    return dictionary

def getFrequency(book, word):
    dictionary = createDictionary(book)
    if not book or not word:
        return -1
    word = word.strip().lower()
    if word in dictionary:
        return dictionary[word]
    else:
        return 0

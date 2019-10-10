# Anthony Gandini

def main():
    sentence = input("Enter a sentence using no punctuation:")
    words = sentence.split(" ")
    
    avgWordLen = 0
    for i in words:
        avgWordLen = avgWordLen + len(i)
        
    avgWordLen = avgWordLen / len(words)
    chars = len(sentence)
    numWords = len(words)
    
    print("Number of characters:" , chars)
    print("Number of words:" , numWords)
    print("Average word length:" , avgWordLen)
    
main()
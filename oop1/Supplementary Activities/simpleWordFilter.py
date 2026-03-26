sentence = input("Enter a sentence: ")
words = sentence.split()

badwords = []
Xword = input("Enter a bad word to censor: ")
badwords.append(Xword)

def filter_words():
    for i in range(len(words)):
        if words[i].lower() in badwords:
            words[i] = "***"
    return " ".join(words)

print(filter_words())
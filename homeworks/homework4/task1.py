a = open("yazkora.txt", "r")
text = a.read().replace("\n", " ").split(".")
answer = open('answer.txt', 'w')
for sent in text:
    for word in sent.split(' '):
        if word.endswith ('yo'):
            answer.write(word)
    answer.write('\n')
answer.close()
